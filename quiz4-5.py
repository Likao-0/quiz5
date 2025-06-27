import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('best_selling_phones.db')
c = conn.cursor()

c.execute("SELECT * FROM phones WHERE manufacturer = 'Nokia'")
results = c.fetchall()  # ვიღებთ ყველა შედეგს
print("Nokia-ს ტელეფონები:")
for row in results:
    print(row)
# კითხულობს ყველა იმ ჩანაწერს, სადაც მწარმოებელია Nokia და ბეჭდავს მათ

manufacturer = input("შეიყვანეთ მწარმოებელი: ")
model = input("შეიყვანეთ მოდელი: ")
form_factor = input("შეიყვანეთ ფორმა (keyboard bar, Slider, Touchscreen): ")
smartphone = input("არის თუ არა სმარტფონი? (TRUE/FALSE): ")
year = int(input("შეიყვანეთ წელი: "))
sold = float(input('შეიყვანეთ გაყიდული ტელეფონების რაოდენობა(მილიონებში): '))

c.execute('''INSERT INTO phones (Manufacturer, Model, FormFactor, Smartphone, Year, UnitsSold_million)
             VALUES (?, ?, ?, ?)''', (manufacturer, model, form_factor, smartphone, year, sold))
conn.commit()
ამატებს მომხმარებლის მიერ შეყვანილი ახალი ტელეფონის მონაცემს ცხრილში

update_model = input("შეიყვანეთ ის მოდელი, რომლის განახლებაც გსურთ: ")
new_form_factor = input("შეიყვანეთ ახალი form_factor ამ მოდელისთვის: ")

c.execute('''UPDATE phones
             SET FormFactor = ?
             WHERE Model = ?''', (new_form_factor, update_model))
conn.commit()
# ცვლის form_factor-ს იმ მოდელისთვის, რომლის სახელიც მომხმარებელმა შეიყვანა

delete_model = input("შეიყვანეთ მოდელი, რომლის წაშლაც გსურთ: ")

c.execute("DELETE FROM phones WHERE model = ?", (delete_model,))
conn.commit()
# წაშლის იმ მოდელის ჩანაწერს ცხრილიდან, რომლის სახელიც შეყვანილია


# # ვიღებთ მონაცემებს მწარმოებლების მიხედვით
c.execute("SELECT manufacturer, COUNT(*) FROM phones GROUP BY manufacturer")
data = c.fetchall()
manufacturers = [row[0] for row in data]
counts = [row[1] for row in data]

plt.figure(figsize=(10,5))
plt.bar(manufacturers, counts, color='skyblue')
plt.title("მწარმოებლების მიხედვით ტელეფონების რაოდენობა")
plt.xlabel("მწარმოებელი")
plt.ylabel("რაოდენობა")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# დიაგრამა აჩვენებს თითოეული მწარმოებლის რამდენი ტელეფონია ბაზაში



plt.figure(figsize=(6,6))
plt.pie(counts, labels=manufacturers, autopct='%1.1f%%')
plt.title("მწარმოებლების წილობრივი განაწილება")
plt.show()
# წრიული დიაგრამა აჩვენებს რა წილი უკავია თითოეულ მწარმოებელს მთლიან მონაცემში



plt.figure(figsize=(8,5))
plt.scatter(range(len(manufacturers)), counts, color='green')
plt.title("მწარმოებლების რაოდენობა ინდექსის მიხედვით")
plt.xlabel("ინდექსი")
plt.ylabel("რაოდენობა")
plt.grid(True)

for i in range(len(manufacturers)):
    plt.text(i, counts[i] + 0.1, manufacturers[i], ha='center', fontsize=9, color='black')

plt.show()

# დიაგრამა აჩვენებს რაოდენობებს ინდექსების შესაბამისად

conn.close()
