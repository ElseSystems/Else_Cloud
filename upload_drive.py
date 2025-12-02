"""
Upload Drive - Sistema Avançado de Upload para Google Drive

Sistema moderno e futurista para upload automático de arquivos para o Google Drive
com interface gráfica intuitiva desenvolvida em PyQt5.

Autor: Samuel Else full stack developer
Licença: MIT
"""

import os
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QFileDialog, 
                           QVBoxLayout, QWidget, QLabel, QProgressBar, QMessageBox, QHBoxLayout)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QPalette, QColor
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import pickle

# Escopos OAuth necessários para acesso ao Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_resource_path(relative_path):
    """Obtém o caminho correto para arquivos de recursos, funcionando tanto como executável quanto como script"""
    try:
        # PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Se não estiver rodando como executável, usa o diretório atual
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def get_credentials_path():
    """Retorna o caminho do credentials.json, procurando em vários locais"""
    # Lista de possíveis locais para o credentials.json
    possible_paths = [
        'credentials.json',  # Diretório atual (quando rodando como script)
        get_resource_path('credentials.json'),  # Dentro do executável (PyInstaller)
        os.path.join(os.path.dirname(sys.executable), 'credentials.json'),  # Mesma pasta do executável
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials.json'),  # Mesma pasta do script
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None

class AuthWorker(QThread):
    finished = pyqtSignal(object)
    error = pyqtSignal(str)

    def __init__(self, action='connect'):
        super().__init__()
        self.action = action

    def run(self):
        try:
            if self.action == 'connect':
                # Encontrar o caminho do credentials.json
                credentials_path = get_credentials_path()
                if not credentials_path:
                    self.error.emit("Arquivo 'credentials.json' não encontrado!\n\n"
                                 "Por favor, coloque o arquivo 'credentials.json' na mesma pasta do executável.")
                    return

                creds = None
                token_file_exists = os.path.exists('token.pickle')
                
                # Tentar carregar token existente
                if token_file_exists:
                    try:
                        with open('token.pickle', 'rb') as token:
                            creds = pickle.load(token)
                    except Exception:
                        # Se não conseguir carregar, remover arquivo corrompido
                        try:
                            os.remove('token.pickle')
                        except:
                            pass
                        creds = None

                # Verificar se precisa renovar ou criar novo token
                if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                        try:
                            # Tentar renovar token expirado
                            creds.refresh(Request())
                        except Exception as refresh_error:
                            # Se refresh falhar (invalid_grant), remover token e fazer nova autenticação
                            error_str = str(refresh_error)
                            if 'invalid_grant' in error_str.lower() or 'bad request' in error_str.lower():
                                try:
                                    os.remove('token.pickle')
                                except:
                                    pass
                                # Fazer nova autenticação completa
                                flow = InstalledAppFlow.from_client_secrets_file(
                                    credentials_path, SCOPES)
                                creds = flow.run_local_server(port=0)
                            else:
                                raise refresh_error
                    else:
                        # Fazer nova autenticação
                        flow = InstalledAppFlow.from_client_secrets_file(
                            credentials_path, SCOPES)
                        creds = flow.run_local_server(port=0)
                    
                    # Salvar novo token
                    with open('token.pickle', 'wb') as token:
                        pickle.dump(creds, token)

                # Verificar credenciais e obter informações do usuário
                service = build('drive', 'v3', credentials=creds)
                user_info = service.about().get(fields='user').execute()
                email = user_info.get('user', {}).get('emailAddress', 'Desconhecido')
                self.finished.emit({'creds': creds, 'email': email})
            else:
                self.finished.emit(None)
        except Exception as e:
            error_msg = str(e)
            # Melhorar mensagem de erro para o usuário
            if 'invalid_grant' in error_msg.lower():
                error_msg = "Token de autenticação inválido ou expirado. Tente conectar novamente."
            elif 'credentials.json' in error_msg.lower():
                error_msg = "Arquivo 'credentials.json' não encontrado ou inválido!"
            self.error.emit(error_msg)

class UploadWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(list)
    error = pyqtSignal(str)

    def __init__(self, folder_path, creds):
        super().__init__()
        self.folder_path = folder_path
        self.creds = creds

    def run(self):
        try:
            service = build('drive', 'v3', credentials=self.creds)
            results = []

            files = [f for f in os.listdir(self.folder_path) 
                    if os.path.isfile(os.path.join(self.folder_path, f))]
            total_files = len(files)

            if total_files == 0:
                self.error.emit("Nenhum arquivo encontrado na pasta selecionada!")
                return

            for i, file_name in enumerate(files):
                file_path = os.path.join(self.folder_path, file_name)
                file_metadata = {'name': file_name}
                media = MediaFileUpload(file_path, resumable=True)
                
                file = service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields='id, webViewLink'
                ).execute()

                results.append(f"{file_name} | {file.get('webViewLink')}")
                self.progress.emit(int((i + 1) / total_files * 100))

            self.finished.emit(results)

        except Exception as e:
            self.error.emit(str(e))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚀 Upload Drive - Futuro Digital")
        self.setGeometry(100, 100, 750, 600)
        
        # Aplicar estilo futurista
        self.apply_futuristic_style()

        # Widget central com fundo gradiente
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        # Título principal
        title = QLabel("⚡ UPLOAD DRIVE")
        title_font = QFont("Arial", 24, QFont.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                color: #00ffff;
                padding: 10px;
                border: none;
            }
        """)
        layout.addWidget(title)

        # Subtítulo
        subtitle = QLabel("Sistema Avançado de Upload para Google Drive")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #888; font-size: 12px; padding-bottom: 10px;")
        layout.addWidget(subtitle)

        # Card de Autenticação
        auth_card = QWidget()
        auth_card.setStyleSheet("""
            QWidget {
                background-color: rgba(20, 20, 40, 200);
                border: 2px solid #00ffff;
                border-radius: 15px;
                padding: 20px;
            }
        """)
        auth_card_layout = QVBoxLayout(auth_card)
        auth_card_layout.setSpacing(15)

        # Título da seção de autenticação
        auth_title = QLabel("🔐 CONEXÃO GOOGLE")
        auth_title_font = QFont("Arial", 14, QFont.Bold)
        auth_title.setFont(auth_title_font)
        auth_title.setStyleSheet("color: #00ffff; padding-bottom: 5px;")
        auth_card_layout.addWidget(auth_title)

        # Status da conta com ícone
        self.account_status = QLabel("⚪ Status: Não conectado")
        self.update_status_style('disconnected')
        auth_card_layout.addWidget(self.account_status)

        # Botões de conexão/desconexão em layout horizontal
        auth_buttons_layout = QHBoxLayout()
        auth_buttons_layout.setSpacing(10)

        self.connect_button = QPushButton("🔗 Conectar Conta")
        self.connect_button.clicked.connect(self.connect_account)
        self.connect_button.setMinimumHeight(45)
        self.connect_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00d4ff, stop:1 #0099ff);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 13px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00ffff, stop:1 #00aaff);
                transform: scale(1.05);
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0099cc, stop:1 #0066aa);
            }
            QPushButton:disabled {
                background: #333;
                color: #666;
            }
        """)
        auth_buttons_layout.addWidget(self.connect_button)

        self.disconnect_button = QPushButton("🔌 Desconectar")
        self.disconnect_button.clicked.connect(self.disconnect_account)
        self.disconnect_button.setEnabled(False)
        self.disconnect_button.setMinimumHeight(45)
        self.disconnect_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff6b6b, stop:1 #ee5a6f);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 13px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff8888, stop:1 #ff6b6b);
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #cc5555, stop:1 #aa4444);
            }
            QPushButton:disabled {
                background: #333;
                color: #666;
            }
        """)
        auth_buttons_layout.addWidget(self.disconnect_button)

        auth_card_layout.addLayout(auth_buttons_layout)
        layout.addWidget(auth_card)

        # Card de Upload
        upload_card = QWidget()
        upload_card.setStyleSheet("""
            QWidget {
                background-color: rgba(20, 20, 40, 200);
                border: 2px solid #ff00ff;
                border-radius: 15px;
                padding: 20px;
            }
        """)
        upload_card_layout = QVBoxLayout(upload_card)
        upload_card_layout.setSpacing(15)

        # Título da seção de upload
        upload_title = QLabel("📤 UPLOAD DE ARQUIVOS")
        upload_title_font = QFont("Arial", 14, QFont.Bold)
        upload_title.setFont(upload_title_font)
        upload_title.setStyleSheet("color: #ff00ff; padding-bottom: 5px;")
        upload_card_layout.addWidget(upload_title)

        # Label para instruções
        self.label = QLabel("📁 Selecione uma pasta com arquivos para fazer upload")
        self.label.setStyleSheet("""
            QLabel {
                color: #ccc;
                font-size: 12px;
                padding: 10px;
                background-color: rgba(255, 0, 255, 10);
                border-radius: 8px;
                border: 1px dashed rgba(255, 0, 255, 30);
            }
        """)
        upload_card_layout.addWidget(self.label)

        # Botão para selecionar pasta
        self.select_button = QPushButton("📂 Selecionar Pasta")
        self.select_button.clicked.connect(self.select_folder)
        self.select_button.setMinimumHeight(45)
        self.select_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #9d4edd, stop:1 #c77dff);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 13px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #b55fff, stop:1 #d88fff);
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #7d3dcc, stop:1 #9d5ddd);
            }
        """)
        upload_card_layout.addWidget(self.select_button)

        # Botão para iniciar upload
        self.upload_button = QPushButton("🚀 Iniciar Upload")
        self.upload_button.clicked.connect(self.start_upload)
        self.upload_button.setEnabled(False)
        self.upload_button.setMinimumHeight(50)
        self.upload_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff00ff, stop:0.5 #00ffff, stop:1 #ff00ff);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 15px;
                font-weight: bold;
                padding: 12px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff33ff, stop:0.5 #33ffff, stop:1 #ff33ff);
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #cc00cc, stop:0.5 #00cccc, stop:1 #cc00cc);
            }
            QPushButton:disabled {
                background: #333;
                color: #666;
                border: 1px solid #555;
            }
        """)
        upload_card_layout.addWidget(self.upload_button)

        # Barra de progresso futurista
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimumHeight(30)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #00ffff;
                border-radius: 10px;
                text-align: center;
                color: white;
                font-weight: bold;
                background-color: rgba(0, 0, 0, 100);
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00ffff, stop:0.5 #ff00ff, stop:1 #00ffff);
                border-radius: 8px;
            }
        """)
        upload_card_layout.addWidget(self.progress_bar)

        layout.addWidget(upload_card)

        # Adicionar espaçador no final
        layout.addStretch()

        self.selected_folder = None
        self.creds = None
        self.current_email = None

        # Verificar se já está conectado ao iniciar
        self.check_connection_status()

    def update_status_style(self, status_type='disconnected'):
        """Atualiza o estilo do status baseado no tipo"""
        if status_type == 'connected':
            self.account_status.setStyleSheet("""
                QLabel {
                    color: #00ff88;
                    font-size: 13px;
                    padding: 8px;
                    background-color: rgba(0, 255, 136, 20);
                    border-radius: 8px;
                    border: 1px solid rgba(0, 255, 136, 50);
                }
            """)
        elif status_type == 'connecting':
            self.account_status.setStyleSheet("""
                QLabel {
                    color: #ffaa00;
                    font-size: 13px;
                    padding: 8px;
                    background-color: rgba(255, 170, 0, 20);
                    border-radius: 8px;
                    border: 1px solid rgba(255, 170, 0, 50);
                }
            """)
        elif status_type == 'error':
            self.account_status.setStyleSheet("""
                QLabel {
                    color: #ff6b6b;
                    font-size: 13px;
                    padding: 8px;
                    background-color: rgba(255, 107, 107, 20);
                    border-radius: 8px;
                    border: 1px solid rgba(255, 107, 107, 50);
                }
            """)
        else:  # disconnected
            self.account_status.setStyleSheet("""
                QLabel {
                    color: #ff6b6b;
                    font-size: 13px;
                    padding: 8px;
                    background-color: rgba(255, 107, 107, 20);
                    border-radius: 8px;
                    border: 1px solid rgba(255, 107, 107, 50);
                }
            """)

    def apply_futuristic_style(self):
        """Aplica estilo futurista à janela principal"""
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #0a0a1a, stop:0.5 #1a1a2e, stop:1 #0a0a1a);
            }
            QWidget {
                background: transparent;
            }
            QMessageBox {
                background-color: #1a1a2e;
                color: #ffffff;
            }
            QMessageBox QLabel {
                color: #ffffff;
                background-color: transparent;
            }
            QMessageBox QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00d4ff, stop:1 #0099ff);
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 8px 20px;
                font-weight: bold;
                min-width: 80px;
            }
            QMessageBox QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00ffff, stop:1 #00aaff);
            }
            QMessageBox QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0099cc, stop:1 #0066aa);
            }
        """)

    def check_connection_status(self):
        """Verifica se já existe uma conexão ativa"""
        try:
            if os.path.exists('token.pickle'):
                try:
                    with open('token.pickle', 'rb') as token:
                        creds = pickle.load(token)
                except Exception:
                    # Token corrompido, remover
                    try:
                        os.remove('token.pickle')
                    except:
                        pass
                    creds = None
                
                if creds and creds.valid:
                    # Tentar atualizar se expirado
                    if creds.expired and creds.refresh_token:
                        try:
                            creds.refresh(Request())
                            with open('token.pickle', 'wb') as token:
                                pickle.dump(creds, token)
                        except Exception:
                            # Se refresh falhar, token inválido - remover
                            try:
                                os.remove('token.pickle')
                            except:
                                pass
                            creds = None
                    
                    if creds and creds.valid:
                        service = build('drive', 'v3', credentials=creds)
                        user_info = service.about().get(fields='user').execute()
                        email = user_info.get('user', {}).get('emailAddress', 'Desconhecido')
                        self.creds = creds
                        self.current_email = email
                        self.account_status.setText(f"🟢 Status: Conectado como {email}")
                        self.update_status_style('connected')
                        self.connect_button.setEnabled(False)
                        self.disconnect_button.setEnabled(True)
                        return
        except Exception:
            # Em caso de qualquer erro, considerar não conectado
            pass
        
        self.account_status.setText("⚪ Status: Não conectado")
        self.update_status_style('disconnected')
        self.connect_button.setEnabled(True)
        self.disconnect_button.setEnabled(False)

    def connect_account(self):
        """Conecta com a conta Google"""
        credentials_path = get_credentials_path()
        if not credentials_path:
            QMessageBox.warning(self, "Arquivo não encontrado", 
                              "O arquivo 'credentials.json' não foi encontrado!\n\n"
                              "Por favor, baixe o arquivo de credenciais do Google Cloud Console\n"
                              "e coloque-o na mesma pasta do executável.")
            return

        self.connect_button.setEnabled(False)
        self.account_status.setText("🟡 Status: Conectando...")
        self.update_status_style('connecting')
        
        self.auth_worker = AuthWorker('connect')
        self.auth_worker.finished.connect(self.auth_success)
        self.auth_worker.error.connect(self.auth_error)
        self.auth_worker.start()

    def auth_success(self, result):
        """Callback quando autenticação é bem-sucedida"""
        if result:
            self.creds = result['creds']
            self.current_email = result['email']
            self.account_status.setText(f"🟢 Status: Conectado como {result['email']}")
            self.update_status_style('connected')
            self.connect_button.setEnabled(False)
            self.disconnect_button.setEnabled(True)
            QMessageBox.information(self, "✅ Sucesso", f"Conectado com sucesso!\n\nConta: {result['email']}")
        else:
            self.auth_error("Erro desconhecido na autenticação")

    def auth_error(self, error_msg):
        """Callback quando há erro na autenticação"""
        self.connect_button.setEnabled(True)
        self.account_status.setText("🔴 Status: Erro na conexão")
        self.update_status_style('error')
        
        # Se o erro for de token inválido, sugerir remover token antigo
        if 'invalid_grant' in error_msg.lower() or 'token' in error_msg.lower():
            reply = QMessageBox.question(self, "Erro na Autenticação", 
                                        f"Erro ao conectar:\n{error_msg}\n\n"
                                        "Deseja remover o token antigo e tentar novamente?",
                                        QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                try:
                    if os.path.exists('token.pickle'):
                        os.remove('token.pickle')
                    QMessageBox.information(self, "Token Removido", 
                                          "Token antigo removido. Tente conectar novamente.")
                except Exception as e:
                    QMessageBox.warning(self, "Aviso", f"Não foi possível remover o token:\n{str(e)}")
        else:
            QMessageBox.critical(self, "Erro", f"Erro ao conectar:\n{error_msg}")

    def disconnect_account(self):
        """Desconecta da conta Google"""
        reply = QMessageBox.question(self, "Desconectar", 
                                   "Deseja realmente desconectar da conta?",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                if os.path.exists('token.pickle'):
                    os.remove('token.pickle')
                self.creds = None
                self.current_email = None
                self.account_status.setText("⚪ Status: Não conectado")
                self.update_status_style('disconnected')
                self.connect_button.setEnabled(True)
                self.disconnect_button.setEnabled(False)
                self.upload_button.setEnabled(False)
                self.selected_folder = None
                self.label.setText("📁 Selecione uma pasta com arquivos para fazer upload")
                self.label.setStyleSheet("""
                    QLabel {
                        color: #ccc;
                        font-size: 12px;
                        padding: 10px;
                        background-color: rgba(255, 0, 255, 10);
                        border-radius: 8px;
                        border: 1px dashed rgba(255, 0, 255, 30);
                    }
                """)
                QMessageBox.information(self, "Desconectado", "Conta desconectada com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao desconectar:\n{str(e)}")

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Selecione a pasta com os arquivos")
        if folder:
            self.selected_folder = folder
            # Truncar caminho muito longo para melhor visualização
            display_path = folder if len(folder) < 60 else "..." + folder[-57:]
            self.label.setText(f"📁 Pasta selecionada:\n{display_path}")
            self.label.setStyleSheet("""
                QLabel {
                    color: #00ff88;
                    font-size: 12px;
                    padding: 10px;
                    background-color: rgba(0, 255, 136, 15);
                    border-radius: 8px;
                    border: 1px solid rgba(0, 255, 136, 40);
                }
            """)
            if self.creds:
                self.upload_button.setEnabled(True)
            else:
                QMessageBox.warning(self, "Não conectado", 
                                  "Por favor, conecte-se a uma conta Google primeiro!")

    def start_upload(self):
        if not self.selected_folder:
            return
        
        if not self.creds:
            QMessageBox.warning(self, "Não conectado", 
                              "Por favor, conecte-se a uma conta Google primeiro!")
            return

        self.upload_button.setEnabled(False)
        self.select_button.setEnabled(False)
        self.connect_button.setEnabled(False)
        self.disconnect_button.setEnabled(False)
        self.progress_bar.setValue(0)

        self.worker = UploadWorker(self.selected_folder, self.creds)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.upload_finished)
        self.worker.error.connect(self.show_error)
        self.worker.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def upload_finished(self, results):
        self.upload_button.setEnabled(True)
        self.select_button.setEnabled(True)
        self.connect_button.setEnabled(False)
        self.disconnect_button.setEnabled(True)
        
        # Salvar resultados em um arquivo de texto com nome da pasta
        try:
            # Pegar o nome da pasta selecionada
            folder_name = os.path.basename(self.selected_folder) if self.selected_folder else "pasta"
            # Remover caracteres inválidos para nome de arquivo
            folder_name = "".join(c for c in folder_name if c.isalnum() or c in (' ', '-', '_')).strip()
            # Se ficar vazio, usar nome padrão
            if not folder_name:
                folder_name = "pasta"
            # Criar nome do arquivo: link + nome da pasta + .txt
            filename = f"link{folder_name}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                for result in results:
                    f.write(result + '\n')
            
            self.label.setText(f"✅ Upload concluído! Links salvos em '{filename}'")
            self.label.setStyleSheet("""
                QLabel {
                    color: #00ff88;
                    font-size: 12px;
                    padding: 10px;
                    background-color: rgba(0, 255, 136, 15);
                    border-radius: 8px;
                    border: 1px solid rgba(0, 255, 136, 40);
                }
            """)
            QMessageBox.information(self, "✅ Sucesso", 
                                  f"Upload concluído com sucesso!\n\n"
                                  f"{len(results)} arquivo(s) enviado(s).\n"
                                  f"Links salvos em '{filename}'")
        except Exception as e:
            QMessageBox.warning(self, "Aviso", 
                              f"Upload concluído, mas erro ao salvar links:\n{str(e)}")

    def show_error(self, error_msg):
        self.upload_button.setEnabled(True)
        self.select_button.setEnabled(True)
        if self.creds:
            self.connect_button.setEnabled(False)
            self.disconnect_button.setEnabled(True)
        else:
            self.connect_button.setEnabled(True)
            self.disconnect_button.setEnabled(False)
        self.label.setText(f"Erro: {error_msg}")
        QMessageBox.critical(self, "Erro no Upload", f"Erro durante o upload:\n{error_msg}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 