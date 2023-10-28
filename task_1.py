import sqlite3 as sql
from sqlite3 import Cursor
from typing import Any


column = str


def averrage_revenue(cur: Cursor, attribute: column) -> list[Any]:
    stmt = cur.execute(
        f"""select {attribute}, avg(revenue) as avg_revenue
                       from pub_works
                       group by {attribute}
                       order by avg_revenue
                       desc"""
    )

    return stmt.fetchall()


def pub_worker_averrage(cur: Cursor) -> list[Any]:
    stmt = cur.execute(
        """select pub, worker, avg(revenue) as avg_revenue
            from pub_works
            group by pub, worker
            order by avg_revenue
            desc"""
    )

    return stmt.fetchall()


if __name__ == "__main__":
    con = sql.connect("pub_works.sqlite")
    cur = con.cursor()

    # DEFAULT WAY
    # _____________________________________________

    print("-----DEFAULT WAY-----")

    pubs_avg = averrage_revenue(cur, "pub")
    workers_avg = averrage_revenue(cur, "worker")

    for pub, worker in zip(pubs_avg, workers_avg):
        print({pub[0]: worker[0]})

    # _____________________________________________

    # MY WAY
    # Ищем для каждого отдельно взятого места самого прибыльного работника
    # _____________________________________________

    print("-----MY WAY-----")

    pubs_workers_avg = pub_worker_averrage(cur)
    pubs_workers = {}

    for pub_worker in pubs_workers_avg:
        if (
            pub_worker[0] not in pubs_workers.keys()
            and pub_worker[1] not in pubs_workers.values()
        ):
            pubs_workers[pub_worker[0]] = pub_worker[1]
            print({pub_worker[0]: pub_worker[1]})

    # _____________________________________________
