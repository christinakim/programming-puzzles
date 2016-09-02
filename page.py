listings = [
# "host_id,listing_id,score,city",
"1,28,300.1,San Francisco",
"4,5,209.1,San Francisco",
"20,7,208.1,San Francisco",
"23,8,207.1,San Francisco",
"16,10,206.1,Oakland",
"1,16,205.1,San Francisco",
"1,31,204.6,San Francisco",
"6,29,204.1,San Francisco",
"7,20,203.1,San Francisco",
"8,21,202.1,San Francisco",
"2,18,201.1,San Francisco",
"2,30,200.1,San Francisco", 
"15,27,109.1,Oakland",
"10,13,108.1,Oakland",
"11,26,107.1,Oakland",
"12,9,106.1,Oakland",
"13,1,105.1,Oakland",
"22,17,104.1,Oakland",
"1,2,103.1,Oakland",
"28,24,102.1,Oakland",
"18,14,11.1,San Jose",
"6,25,10.1,Oakland",
"19,15,9.1,San Jose",
"3,19,8.1,San Jose",
"3,11,7.1,Oakland",
"27,12,6.1,Oakland",
"1,3,5.1,Oakland",
"25,4,4.1,San Jose",
"5,6,3.1,San Jose",
"29,22,2.1,San Jose",
"30,23,1.1,San Jose"
]

class Listing:
    def __init__(self, host_id, listing_id, score, city):
        self.host_id = host_id
        self.listing_id = listing_id
        self.score = score
        self.city = city

def page(n):
    listings = []
    for i in n:
        str_arr = i.split(",")
        str_arr[2] = float(str_arr[2])
        #listing = Listing(str_arr[0],str_arr[1], str_arr[2], str_arr[3])
        listings.append(str_arr)

    listings = sorted(listings, key = lambda l: (l[2]), reverse = True)
    seen = set()
    page = [[]]
    listingsLeft = []
    cnt = 0
    i = 0 
    while len(listings) > 0:
        while cnt < 10 and i < len(listings):
            if listings[i][0] not in seen:
                seen.add(listings[i][0])
                page[-1].append(listings[i])
                i += 1
                cnt += 1
            else:
                i += 1
                listingsLeft.append(listings[i])
        if i != len(listings):
            page.append([])
        listings = listingsLeft + listings[i:]
        seen = set()
        listingsLeft = []
        cnt = 0
        i = 0

    return page


for i in page(listings)

