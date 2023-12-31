
# The function tax_price takes an input of an item's price and multiplies it by the sales tax
# of California. The function returns the final_price variable, which contains the product of the
# inputted price and the sales tax rate.
def tax_price(price):
    tax_rate = 0.0725
    sales_tax = price * tax_rate
    final_price = price + sales_tax
    return final_price


# The function find_item_prices takes three inputs: store_items (list), store_prices (list), select_item (string).
# The store_items and store_prices lists must have corresponding indexes, as the prices and products
# need to match up. If possible, a dictionary may be used to simplify this function.
# This function takes the desired search item, finds where the item is in the list, takes the index
# of the item, and then returns the value of that index in the price list.
def find_item_price(store_items, store_prices, select_item):
    search = select_item
    price = 0
    for i in store_items:
        if store_items[i] == search:
            price = store_prices[i]
    return price


# The function median_income takes two inputs: geographic_data, which is a list that contains
# dictionaries, and a region, which is a string. The geographic_data is a database that contains
# income data of several regions and their subregions. The function first creates an empty list
# to ultimately calculate the median. The list is filled with values appended from the geo
# dictionaries, where if the region matches the input, the value of the income key is added to
# the empty list. The median
def median_income(geographic_data, region):
    geo = geographic_data
    median_list = []
    for i in geo:
        if geo[i]["region"] == region:
            median_list.append(geo[i]["income"])

    median_list.sort()
    if len(median_list) % 2 == 0:
        med_index = len(median_list) // 2
        median = (median_list[med_index+1] + median_list[med_index])/2
        return median
    else:
        med_index = (len(median_list) // 2)+1
        median = (median_list[med_index])
        return median


# The function overlap_region takes a geographical database, searches through its city entries, and
# finds if the city is a part of the inputted region. If the region of the city and the input
# region matches, then the city will be appended to a list that will be the output.
def overlap_region(geographic_data, region):
    geo = geographic_data
    city_list = []
    for i in geo:
        if geo[i]["city"]["region"] == region:
            city_list.append(geo[i]["city"])

    return city_list


