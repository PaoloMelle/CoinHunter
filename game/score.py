import os


class ScoreManager:

    EASY_FILE = "data/scores_easy.txt"
    HARD_FILE = "data/scores_hard.txt"

    @staticmethod
    def _ensure_file(file_path):

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write("")

    @staticmethod
    def save_score(score, mode):

        file_path = (
            ScoreManager.EASY_FILE
            if mode == "easy"
            else ScoreManager.HARD_FILE
        )

        ScoreManager._ensure_file(file_path)

        scores = ScoreManager.load_scores(mode)

        scores.append(score)
        scores.sort(reverse=True)
        scores = scores[:5]

        with open(file_path, "w") as file:
            for value in scores:
                file.write(f"{value}\n")

    @staticmethod
    def load_scores(mode):

        file_path = (
            ScoreManager.EASY_FILE
            if mode == "easy"
            else ScoreManager.HARD_FILE
        )

        ScoreManager._ensure_file(file_path)

        scores = []

        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    scores.append(int(line))

        return scores