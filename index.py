import re

def validate_credit_card(number):
    # Remove espaços e traços
    sanitized_number = re.sub(r'[\s-]', '', number)

    # Verifica se o número contém apenas dígitos
    if not re.match(r'^\d+$', sanitized_number):
        return {'valid': False, 'bandeira': None}

    # Verifica o comprimento do número do cartão
    if len(sanitized_number) < 13 or len(sanitized_number) > 19:
        return {'valid': False, 'bandeira': None}

    # Determina a bandeira do cartão
    bandeira = get_card_type(sanitized_number)

    # Validação do número do cartão usando o algoritmo de Luhn
    is_valid = luhn_check(sanitized_number)

    return {'valid': is_valid, 'bandeira': bandeira}

def get_card_type(number):
    card_types = {
        'visa': r'^4[0-9]{12}(?:[0-9]{3})?$',
        'mastercard': r'^5[1-5][0-9]{14}$',
        'amex': r'^3[47][0-9]{13}$',
        'discover': r'^6(?:011|5[0-9]{2})[0-9]{12}$',
        'diners': r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
        'jcb': r'^(?:2131|1800|35\d{3})\d{11}$',
        'elo': r'^((636368)|(438935)|(504175)|(451416)|(636297)|(5067)|(4576)|(4011))\d+$',
        'hipercard': r'^(606282\d{10}(\d{3})?)|(3841\d{15})$'
    }

    for card_type, pattern in card_types.items():
        if re.match(pattern, number):
            return card_type.capitalize()

    return 'Unknown'

def luhn_check(number):
    sum = 0
    should_double = False

    for digit in reversed(number):
        digit = int(digit)

        if should_double:
            digit *= 2
            if digit > 9:
                digit -= 9

        sum += digit
        should_double = not should_double

    return sum % 10 == 0

# Solicita que o usuário insira o número do cartão de crédito
card_number = input("Por favor, insira o número do cartão de crédito: ")
result = validate_credit_card(card_number)
print(result) # Exibe o resultado da validação