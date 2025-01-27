import datetime
while True:
    print("AVAILABLE MOVIES:\n1.BARROZ\n2.REKHACHITRAM\n3.MARCO\nchoose from 1 -3")
    movie=int(input().strip())
    no_ticket=int(input("enter the no of tickets\n").strip())
    ticket_type=input("select 1.premium 2.normal\n").strip()
    print("select showtime")
    show_time=input("1. 10:00\n2. 1:30\n3. 6:00\n4. 9:30\n")
    premium=200
    cost=0
    discount=0
    normal=150
    if ticket_type==1:
        cost=premium*no_ticket
    else:
        cost=normal*no_ticket
    if no_ticket>=5:
        discount= 0.1*cost
    cost-=discount
    print("TICKET DETAILS:")
    if movie==1:
        print("movie name:BARROZ")
    elif movie==2:
        print("movie name:REKHACHITRAM")
    else:
        print("movie name:MARCO")
    print("Quantity:"+str(no_ticket))
    if ticket_type==1:
        print("Ticket Type: premium")
    else:
        print("Ticket Type:normal")
    if show_time==1:
        print("Time:10:00")
    elif show_time==2:
        print("Time:1:30")
    elif show_time==3:
        print("Time:6:00")
    else:
        print("Time:9:30")
    print("Date:" + str(datetime.date.today()))
    print("Total cost:"+str(cost))
    ch=input("Enter 'Y' to book more ticket else 'N'").lower().strip()
    if ch=="n":
        print("See you soon!!!\n")
        break









