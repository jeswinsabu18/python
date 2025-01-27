def pcm_cal(name,phy,chem,maths):
    avg=(int(phy)+int(chem)+int(maths))/3
    print(str(name))
    print(f"percentage of pcm={avg:.2f}")
    return avg

name=input("Enter your name:")
phy=input("Enter the marks of physics:")
chem=input("Enter the marks of chemistry:")
maths=input("Enter the marks of maths:")
avg=pcm_cal(name,phy,chem,maths)
report_card_content=f"""
---------------------------------------------------------------------------------------------------
                                       {name}'s  REPORT CARD
---------------------------------------------------------------------------------------------------
PHYSICS MARK:{phy}
CHEMISTRY MARK:{chem}
MATHS MARK:{maths}
PERCENTAGE %={avg:.2f}
"""
filename=f"{name}_report_card"

with open(filename,"w")as f:
    f.write(report_card_content)