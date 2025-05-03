import Lab2_DOAIOT.Lab2 as bmi


def test_bmi_normal_weight():
    input_height = 1.73
    input_weight = 60
    input_bmi = bmi.calculate_BMI(input_height, input_weight)

    value = 0
    result = bmi.classify_BMI(input_bmi)

    assert (result == value)

def test_bmi_over_weight():
    input_height = 1.50
    input_weight = 80
    input_bmi = bmi.calculate_BMI(input_height, input_weight)

    value = 1
    result = bmi.classify_BMI(input_bmi)

    assert (result == value)



def test_bmi_under_weight():
    input_height = 1.85
    input_weight = 60
    input_bmi = bmi.calculate_BMI(input_height, input_weight)

    value = -1
    result = bmi.classify_BMI(input_bmi)

    assert (result == value)
