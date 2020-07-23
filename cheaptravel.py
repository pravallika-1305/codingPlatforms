
total_rides,rides,sprice,rupees = map(int,input().split())
 
if(rupees / rides > sprice) and total_rides > rides:
    print(sprice * total_rides)
elif total_rides < rides:
    if sprice * total_rides > rupees:
        print(rupees)
    else:
        print(sprice * total_rides)
else:
    base_fare = (total_rides // rides) * rupees
    if rupees < sprice * (total_rides % rides):
        cement_fare = rupees
    else :
        cement_fare = sprice * (total_rides % rides)
    print(base_fare + cement_fare)