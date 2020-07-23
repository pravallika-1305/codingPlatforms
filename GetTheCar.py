def Months(startPOld, startPNew, savingperMonth, percentLossMonth):
    month = 0
    savings = 0

    while startPOld + savings < startPNew:
        month += 1
        savings += savingperMonth
        if month % 2 == 0:
            percentLossMonth += 0.5

        startPOld *= ((100 - percentLossMonth) / 100)
        startPNew *= ((100 - percentLossMonth) / 100)

    return([month, round(float(startPOld) + float(savings) - float(startPNew),2)])
spo = int(input())
spn = int(input())
spm = int(input())
plm = float(input())
print(Months(spo,spn,spm,plm))
