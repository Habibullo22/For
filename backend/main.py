from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db = sqlite3.connect("users.db", check_same_thread=False)
cursor = db.cursor()

@app.get("/balance/{user_id}")
def get_balance(user_id: int):
    cursor.execute(
        "SELECT usdt, rub, uzs FROM users WHERE user_id=?",
        (user_id,)
    )
    row = cursor.fetchone()
    if not row:
        raise HTTPException(404, "User not found")

    return {
        "usdt": row[0],
        "rub": row[1],
        "uzs": row[2]
    }

@app.post("/admin/add_balance")
def add_balance(user_id: int, usdt: float = 0, rub: float = 0, uzs: int = 0, admin_id: int = 0):
    if admin_id != 5815294733:
        raise HTTPException(403, "Not admin")

    cursor.execute("""
        UPDATE users
        SET usdt = usdt + ?,
            rub = rub + ?,
            uzs = uzs + ?
        WHERE user_id = ?
    """, (usdt, rub, uzs, user_id))
    db.commit()

    return {"status": "ok"}
