from ignorant.modules.social_media.instagram import instagram
import trio
import httpx
import time
import sqlite3
conn=sqlite3.connect('phone.db')

phone="9120218638"
country_code="98"

async def main():

    client = httpx.AsyncClient()
    out = []

    await instagram(phone, country_code, client, out)
    print(out[0])
    if out[0]['exists']==True:
        x = conn.execute("SELECT * FROM iran_numbers WHERE number='" + country_code+phone + "'").fetchone()
        if x is None:
            conn.execute("INSERT INTO iran_numbers (number) VALUES ('" + country_code+phone + "')")
            print(phone, ' - inserted')
            conn.commit()
        else:
            print(phone, ' - exists')

    await client.aclose()

for i in range(9120218651,9120200000,-1):
    time.sleep(1)
    phone=str(i)
    trio.run(main)