url= 'http://ww.sougou.com/s?'
def sougou(nets):
    count = 1 
    for net in nets:
        rest1 = 'res%d.txt' %count
        with open(rest1,'w',encoding='utf8') as f:
            f.write(net)
        print(net)
        count +=1
if __name__ == '__main__':
    nets = ('one','two','pr')
    sougou(nets)