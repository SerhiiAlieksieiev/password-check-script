import urwid

def is_very_long(password):
    return len(password) > 12

def has_digit(password):
  return any(character.isdigit() for character in password)

def has_letters(password):
    return any(not letter.isdigit() for letter in password)

def has_upper_letters(password):
    return any(letter.isupper() for letter in password) 

def has_lower_letters(password):
    return any(letter.islower() for letter in password)
    
def has_symbols(password):
    return any(character.isdigit() and not character.isalpha() for character in password)

def doesnt_consist_of_symbols(password):
    return any(character.isdigit() or character.isalpha() for character in password)

def on_ask_change(edit, new_edit_text):
    score = 0
    for callback in callbacks:
        if callback(new_edit_text):
            score += 2
    reply.set_text("Рейтинг пароля: {}".format(score))

if __name__ == '__main__':
    callbacks = [is_very_long, has_digit, has_letters, has_upper_letters,
                 has_lower_letters, has_symbols, doesnt_consist_of_symbols]
    ask = urwid.Edit('Тайный ввод: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
