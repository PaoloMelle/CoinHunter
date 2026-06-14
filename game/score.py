import os

# Gerencia o armazenamento e leitura das pontuações do jogo
class ScoreManager:

    EASY_FILE = "data/scores_easy.txt"
    HARD_FILE = "data/scores_hard.txt"

# Salva uma pontuação no ranking correspondente ao modo de jogo
    @staticmethod
    def save_score(score, mode):

        file_path = (
            ScoreManager.EASY_FILE
            if mode == "easy"
            else ScoreManager.HARD_FILE
        )

        scores = ScoreManager.load_scores(mode)

        scores.append(score)

        scores.sort(reverse=True)

        scores = scores[:5]

        with open(file_path, "w") as file:

            for value in scores:

                file.write(f"{value}\n")

    # Carrega as pontuações armazenadas para o modo informado
    @staticmethod
    def load_scores(mode):

        file_path = (
            ScoreManager.EASY_FILE
            if mode == "easy"
            else ScoreManager.HARD_FILE
        )

        if not os.path.exists(file_path):
            return []

        with open(file_path, "r") as file:

            scores = []

            for line in file:

                line = line.strip()

                if line:

                    scores.append(
                        int(line)
                    )

            return scores