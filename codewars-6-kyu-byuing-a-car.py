def nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):

    saving = 0
    price_of_old_car = start_price_old
    price_of_new_car = start_price_new
    months = 0
    if price_of_new_car <= price_of_old_car:
        return [0, price_of_old_car - price_of_new_car]
    while True:
        months += 1
        if months > 1 and months % 2 == 0:
            percent_loss_by_month += 0.5
        saving += saving_per_month
        price_of_new_car -= price_of_new_car*(percent_loss_by_month/100)
        price_of_old_car -= price_of_old_car*(percent_loss_by_month/100)
        print(months, price_of_old_car, price_of_new_car, saving)
        if price_of_old_car + saving >= price_of_new_car:
            charge = round(price_of_old_car + saving - price_of_new_car)
            return [months, charge]
        
print(nb_months(2000, 8000, 1000, 1.5))
