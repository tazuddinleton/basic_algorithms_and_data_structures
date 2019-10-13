namespace game_of_life {
    using System;
    class Program {
        static void Main (string[] args) {
            GameOfLife game = new GameOfLife (5, 5);
            game.Initialize ();
        }
    }

    class GameOfLife {
        int max_row;
        int max_col;

        int[, ] community;
        int[, ] newCommunity;

        public GameOfLife (int col, int row) {
            max_col = col;
            max_row = row;
        }
        public void Initialize () {
            System.Console.WriteLine ("Specify initial community : ");
            community = new int[max_col, max_row];
            for (int i = 0; i < max_col; i++) {
                for (int j = 0; j < max_row; j++) {
                    community[i, j] = int.Parse (System.Console.ReadLine ());
                }
            }

            System.Console.WriteLine ("You specified the following : ");
            Render (community);

            while (UserSaysYes ()) {
                newCommunity = new int[max_col, max_row];
                for (int i = 0; i < max_col; i++) {
                    for (int j = 0; j < max_row; j++) {
                        switch (NeighourCount (i, j)) {
                            case int n when n >= 0 && n <= 1:
                                newCommunity[i, j] = 0;
                                break;
                            case 2:
                                newCommunity[i, j] = community[i, j];
                                break;
                            case 3:
                                newCommunity[i, j] = 1;
                                break;
                            case int n when n >= 4 && n <= 8:
                                newCommunity[i, j] = 0;
                                break;
                        }
                    }
                }
                Render (newCommunity);
                community = newCommunity;
            }
        }

        private bool UserSaysYes () {
            System.Console.WriteLine ("Do you want continue viewing next generation ?");
            string userInput = System.Console.ReadLine ();
            while (userInput != "yes" && userInput != "no") {
                System.Console.WriteLine ("Invalid answer, you can only type yes or no");
                userInput = System.Console.ReadLine ();
            }
            if (userInput == "no") {
                return false;
            }
            return true;
        }

        private int NeighourCount (int row, int col) {
            int count = 0;
            int startRow = row - 1 < 0 ? 0 : row - 1;
            int startCol = col - 1 < 0 ? 0 : col - 1;

            int endRow = row + 1 > max_row ? row : row + 1;
            int endCol = col + 1 > max_col ? col : col + 1;

            for (int i = startRow; i < endRow; i++) {
                for (int j = startCol; j < endCol; j++) {
                    if (community[i, j] == 1) {
                        count++;
                    }
                }
            }
            return count;
        }

        private void Render (int[, ] community) {
            string str = "";
            for (int i = 0; i < max_col; i++) {
                str += "\n";
                for (int j = 0; j < max_row; j++) {
                    str += community[i, j].ToString ();
                }
            }
            System.Console.WriteLine (str);
        }
    }
}