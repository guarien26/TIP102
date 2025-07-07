def average_nft_value(nft_collection):

    totalsum = 0 # O(1)

    if len(nft_collection) == 0: #O(1)
        return 0
    else:
        for nft in nft_collection: #O(n)
            totalsum += nft["value"]
        return totalsum / len(nft_collection)
            
# space complexity O(1)
# time complexity O(1)





nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))