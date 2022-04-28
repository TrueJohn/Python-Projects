def verify_vector(name_id, color, type_of_vector, values):
    try:
        int(name_id)
    except ValueError:
        print("The name id must be an integer")

    else:
        try:
            type_of_vector1 = int(type_of_vector)
            if type_of_vector1 < 1:
                raise ValueError
        except ValueError:
            print("Type must be a positive integer grater or equal to 1")

        else:
            try:
                if not isinstance(values, list) :
                    raise ValueError
                else:
                    for i in range(len(values)):
                        if not isinstance(values[i], int):
                            raise ValueError
            except ValueError:
                print("Values must be a non empty list of numbers")

            else:
                try:
                    colors = ['r', 'g', 'b', 'y', 'm']
                    ok = 0
                    for item in colors:
                        if color == item:
                            ok = 1
                    if ok == 0:
                        raise ValueError
                except ValueError:
                    print('Colors must be one of the following : r , g , b, y, m')

                else:
                    return True
