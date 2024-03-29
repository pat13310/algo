import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout,QHBoxLayout, QWidget, QLabel, QMessageBox
from PySide6.QtGui import QPalette, QColor, QRadialGradient

class Morpion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.current_player="X"
        self.setWindowTitle('Morpion')
        self.setGeometry(100, 100, 300, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Tour du joueur X", self)
        self.layout.addWidget(self.label)

        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            row_layout = QHBoxLayout()
            for j in range(3):
                button = QPushButton('', self)
                button.setFixedSize(90, 90) 
                self.set_button_style(button)
                button.clicked.connect(lambda checked=False, row=i, col=j: self.button_clicked(row, col))
                row_layout.addWidget(button)
                self.buttons[i][j] = button
                
            self.layout.addLayout(row_layout)

        self.central_widget.setLayout(self.layout)

        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.game_over = False

    def button_clicked(self, row, col):
        if not self.game_over and self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
        palette = QPalette()
        if self.current_player == 'X':
            text_color = QColor('green')
        else:
            text_color = QColor('red')

        palette.setColor(QPalette.ButtonText, text_color)
        self.buttons[row][col].setPalette(palette)

        if self.check_winner():
            self.show_winner()
        elif self.check_full():
            self.show_match_nul()
        else:
            self.toggle_player()

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.label.setText(f"Tour du joueur {self.current_player}")

    def check_winner(self):
        # on verifie en colonnes et rangees
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.current_player \
                    or self.board[0][i] == self.board[1][i] == self.board[2][i] == self.current_player:
                self.game_over = True
                return True
        # on verifie en diagonale
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player \
                or self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            self.game_over = True
            return True

        return False
    # on regarde si les cases sont toutes remplies
    def check_full(self):
        return not any('' in row for row in self.board)
        #return all(all(cell != '' for cell in row) for row in self.board)
    # match gagnant
    def show_winner(self):
        QMessageBox.information(self, 'Partie terminée', f'Le joueur {self.current_player} a gagné!')
        self.reset_game()
    # match nul
    def show_match_nul(self):
        QMessageBox.information(self, 'Partie terminée', 'Match nul!')
        self.reset_game()
    # on remet à zero le jeu
    def reset_game(self):
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.game_over = False

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText('')
                self.set_button_style(self.buttons[i][j])

        self.label.setText(f"Tour du joueur {self.current_player}")


    def set_button_style(self, button):
        
        style = """
        QPushButton {
            background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5,
                                        stop: 0 #2e2e2e, stop: 1 #3c3c3c);
            border: 2px solid #3c3c3c;
            border-radius: 10px;            
            font-size: 18px;
            font-weight: bold;
        }
        QPushButton:hover {
            background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5,
                                        stop: 0 #3c3c3c, stop: 1 #5a5a5a);
        }
        QPushButton:pressed {
            background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5,
                                        stop: 0 #1e1e1e, stop: 1 #5a5a5a);
        }
        """
        button.setStyleSheet(style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    morpion = Morpion()
    morpion.show()
    sys.exit(app.exec())
