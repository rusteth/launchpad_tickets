def winning_tickets(ticket_numbers, winning_ends):
    winning_tickets = []

    for line in ticket_numbers:
        tickets_in_line = line.split()  # Разделение строки на отдельные билеты
        for ticket in tickets_in_line:
            for end in winning_ends:
                if ticket.endswith(str(end)):  # Проверка, заканчивается ли билет на выигрышное число
                    winning_tickets.append(ticket)
                    break  # Если нашли совпадение, переходим к следующему билету
    return winning_tickets

def main():
    # Имя файла, где хранятся выигрышные номера
    winning_ends_file = "winning_ends.txt"

    try:
        with open(winning_ends_file, 'r') as file:
            winning_ends = [line.strip() for line in file if line.strip()]  # Читаем каждую строку из файла

        # Имя файла, где хранится список ваших билетов
        file_name = "tickets.txt"

        with open(file_name, 'r') as file:
            ticket_numbers = []
            for line in file:
                line = line.strip()
                for word in line.split():  # Разделяем каждую строку на слова и проверяем их
                    if word.isdigit():  # Проверяем, является ли слово числом
                        ticket_numbers.append(word)
    except FileNotFoundError:
        print("Файл не найден.")
        return

    # Найдите выигрышные билеты
    winning_tickets_list = winning_tickets(ticket_numbers, winning_ends)

    # Выведите результат
    if len(winning_tickets_list) > 0:
        print("Выигрышные билеты:")
        for ticket in winning_tickets_list:
            print(ticket)

        # Общее количество билетов
        total_tickets = sum(len(line.split()) for line in ticket_numbers)
        # Количество выигрышных билетов
        num_winning_tickets = len(winning_tickets_list)
        # Процент прохождения билетов
        pass_rate = (num_winning_tickets / total_tickets) * 100

        # Выводим значения с зеленым цветом
        print(f"\nОбщее количество билетов: \033[92m{total_tickets}\033[0m")
        print(f"Количество выигрышных билетов: \033[92m{num_winning_tickets}\033[0m")
        print(f"Процент проходки: \033[92m{pass_rate:.2f}%\033[0m")
    else:
        print("Нет выигрышных билетов.")

if __name__ == "__main__":
    main()