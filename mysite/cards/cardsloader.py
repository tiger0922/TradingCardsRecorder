from cards.models import Card

Mlist = ['Nayeon', 'Jeongyeon', 'Momo', 'Sana', 'Jihyo', 'Mina', 'Dahyun', 'Chaeyoung', 'Tzuyu']
for member in Mlist:
    c = Card(number=91+Mlist.index(member), member=member, piece=0, album="More & more")
    c.save()

