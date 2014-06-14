from sys import argv

def dictionary(filename):
    # getting the argument and assigning it to a variable
    my_file = open(filename)
    # creating an empty dictionary called restaurants
    restaurants = {}
    # removing the white spaces and separate values for keys and values
    # remember that the for loop will iterate over each line
    # as the first thing to do. Each line in the file will always be string.
    for line in my_file:
        line = line.rstrip()
        data = line.split(':')
        # assigning values to name and rating
        name = data[0]
        rating = data[1]
        # assigning keys and values to the restaurants dictionary.
        restaurants[name] = rating
    # returning the dictionary
    return restaurants

def sort_key(restaurants):
    # getting the argument and assigning it to a variable
    # use a type converter, list(), to convert the keys into a list
    # you must use list because you cannot sort a dictionary, but a list
    restaurants_keys = list(restaurants.keys())
    # sorting list
    restaurants_keys.sort()
    # returning the sorted list
    return restaurants_keys

def print_restaurant_rating(sorted_key, restaurants):
    # looping over the key with a for loop with two arguments
    for key in sorted_key:
        # prints out the stmts about the restaurants and their ratings
        print "The restaurant named %s has a rating of %s" % (key, restaurants[key])
    # end program

def main():
    # begin program
    script, filename = argv
    # calling on the function dictionary(), then assigning it to a variable
    restaurants = dictionary(filename)

    #calling on the function sort_key(), then assigning it to a variable
    sorted_key = sort_key(restaurants)

    # calling on a function to take two arguments and print stmts
    print_restaurant_rating(sorted_key, restaurants)

if __name__ == "__main__":
    main()