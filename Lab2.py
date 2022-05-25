import statistics

def get_user_input():
    input_string = input('Enter elements of a list separated by , ')
    print("\n")
    user_list = input_string.split(",")
    # print list
    print('list: ', user_list)
    newlist= []

    #["1", "7", "3"]
    # convert each item to int type
    for element in user_list:
        # convert each item to int type
        newlist.append(int(element))


    # Calculating the sum of list elements
    print("Sum = ", sum(newlist))


    return newlist


def calc_avg(numbers):
    averageb = sum(numbers) / len(numbers)
    print("Average = ",averageb)
    return
def find_min_max(list):
    print("Minimum= ", min(list))
    print("Maximum= ", max(list))
def calc_median_temperature(list):

    print("the median is ",statistics.median(list))
def sort_temperature(list):
    list.sort()
    print("list sorted= ",list)




def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()

    num_list = get_user_input()
    calc_median_temperature(num_list)


    calc_avg(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    print("bye")

if __name__ == "__main__":
    main()
