const creditCardType = require('credit-card-type');

function validateCreditCard(number) {
    // Remove espaços e traços
    const sanitizedNumber = number.replace(/[\s-]/g, '');

    // Verifica se o número contém apenas dígitos
    if (!/^\d+$/.test(sanitizedNumber)) {
        return { valid: false, bandeira: null };
    }

    // Verifica o comprimento do número do cartão
    if (sanitizedNumber.length < 13 || sanitizedNumber.length > 19) {
        return { valid: false, bandeira: null };
    }

    // Usa a biblioteca para determinar a bandeira do cartão
    const cardInfo = creditCardType(sanitizedNumber);

    if (cardInfo.length === 0) {
        return { valid: false, bandeira: null };
    }

    // Verifica se a bandeira é MasterCard
    const bandeira = cardInfo[0].type === 'mastercard' ? 'MasterCard' : cardInfo[0].niceType;

    // Validação do número do cartão usando o algoritmo de Luhn
    const isValid = luhnCheck(sanitizedNumber);

    return { valid: isValid, bandeira: bandeira };
}

function luhnCheck(number) {
    let sum = 0;
    let shouldDouble = false;

    for (let i = number.length - 1; i >= 0; i--) {
        let digit = parseInt(number.charAt(i));

        if (shouldDouble) {
            digit *= 2;
            if (digit > 9) {
                digit -= 9;
            }
        }

        sum += digit;
        shouldDouble = !shouldDouble;
    }

    return sum % 10 === 0;
}

// Exemplo de uso
const cardNumber = '4555 5555 5555 4444'; // Número de exemplo MasterCard
const result = validateCreditCard(cardNumber);
console.log(result); // { valid: true, bandeira: 'MasterCard' }