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

    print("Minimum= ",min(newlist))
    print("Maximum= ",max(newlist))

    average = sum(newlist) / len(newlist)
    print("Average = ", average)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()

    num_list = get_user_input()

if __name__ == "__main__":
    main()
