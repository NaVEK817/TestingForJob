class ABCustomers:
    def countAB(self, n_customers, n_first_id = None):
        if n_first_id is None:
            print("A = ", (n_customers//2 + n_customers % 2), "B = ",(n_customers//2))
        else:
            print("A = ", n_customers//2 + ((n_customers % 2) >= (n_first_id%2)), "B = ", (n_customers//2))

Result = ABCustomers()
while True:
    print('Введите количество пользователей')
    n_customers = int(input())

    Result.countAB(n_customers)

    print('Введите количество пользователей и начальный id')
    n_customers = int(input())
    n_first_id = int(input())
    Result.countAB(n_customers, n_first_id)
        

