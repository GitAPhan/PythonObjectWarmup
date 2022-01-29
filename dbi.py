import dbcreds
import mariadb as db


class DbInteraction:

    def display_scoreboard():
        conn = db.connect(user=dbcreds.user,
                          password=dbcreds.password,
                          host=dbcreds.host,
                          port=dbcreds.port,
                          database=dbcreds.database)
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT count(*) as wins FROM python_fighter.fight_result where win=1")
        win_count = cursor.fetchone()

        cursor.execute(
            f"SELECT count(*) as wins FROM python_fighter.fight_result where win=0")
        loss_count = cursor.fetchone()

        cursor.close()
        conn.close()

        print(f"Scoreboard")
        print(f"Player: {win_count[0]}")
        print(f"Computer: {loss_count[0]}")

    def add_win_loss_to_db(result):
        conn = db.connect(user=dbcreds.user,
                          password=dbcreds.password,
                          host=dbcreds.host,
                          port=dbcreds.port,
                          database=dbcreds.database)
        cursor = conn.cursor()

        cursor.execute(f"insert into fight_result(win) values({result})")
        conn.commit()

        cursor.close()
        conn.close()
