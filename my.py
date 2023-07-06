def main():
    a=[roll_dice,move,combat,get_coins,buy_health,print_status]
    i=0
    while i<len(a):
        a[i%len(a)]()
        i+=1