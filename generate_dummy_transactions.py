import csv
import datetime
from database.DataLayer import DataLayer

# open csv
with open("dummy_transaction_data.csv", mode="r", encoding="utf-8-sig") as data:
    reader = csv.DictReader(data)

    insert_command = (
        " INSERT INTO transactions (date, category, amount, description, type)"
        "VALUES (%s, %s, %s, %s, %s)"
    )

    # generate MySQL values
    for transaction in reader:
        values = (
            datetime.datetime.strptime(
                transaction["Posting Date"], '%m/%d/%Y').strftime('%Y/%m/%d'),
            transaction["Category"],
            transaction["Amount"],
            transaction["Description"],
            "charge" if "-" in transaction["Amount"] else "deposit"
        )

        # pass command datalayer obj
        data_layer = DataLayer()
        data_layer.execute(insert_command, values)
data_layer.show_all_rows()
print("Successfully inserted")
