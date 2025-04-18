# import streamlit as st
# # # UNIT CONVERTOR APPLICATION (PTOJECT!)Basic level for assignment
# # # INPUT FOR UNIT CONVENTOR APPLICATION ; 
# # # OUTPUT GIVEN BY UNIT CONVERTOR APPLICATION

# # # INPUT
# # # I- (VALUE)
# # # unit from conversion/ ise hame unit ma convert karna he
# # # value 
# # #  2000 meters kilometers
# # # coverted value in 

# def converte_units(value: float, unit_from: str, unit_to: str):
#     # print("value>>>",value)
#     # print("unit_from>>>",unit_from)
#     # print("unit_to>>>",unit_to)
# # # 1 kilometer = 1000 meters
# # # 1 meters = 0.001 kilometers
# # # 1 kilometers = 1000 grams
# # # 1 gram = 0.001 kilogram
# # #    value jo ho wo kilometers me or jis ma convert karna he wo  meters ma
#     if unit_from == "kilometers" and unit_to == "meters":
#         #     1.5 *   1000
#         return value * 1000
#     elif unit_from == "meters" and unit_to == "kilometers":
#         #       1    * 0.001
#         return value * 0.001
#     elif unit_from == "kilograms" and unit_to == "grams":
#                # 2   * 1000
#         return value * 1000
#     elif unit_from == "grams" and unit_to == "kilograms":
#         #
#         return value * 0.001
    
#     else:
#         return "conversion is not supported kindly!"
 




# # result = output ki value ko store karna he
# # result1 = converte_units(1.5, "kilometers","meters")
# # print("result value is", result1)
# # result2 = converte_units(5000, "grams", "kilograms")
# # print("The value is kilograms", result2)

# def main():
#     st.title("Unit Convertor")
#     st.write("Welcome to unit convertor!")
#     print("Unit Convertor!")
#     print("Welcome to unit convertor!")
#     value = st.number_input("Enter the value of you want to convert:", min_value=0.0)
#     unit_from = st.text_input("Enter the unit_from you want to convert from: e.g; meters, kilometers, grams, kilograms")
#     unit_to = st.text_input("Enter the unit_to you want to convert from: e.g; meters, kilometers, grams, kilograms")
    
#     if st.button("convert"):
#          result = converte_units(value, unit_from,unit_to)
#          st.write("converted value is:", result)

    # result = converte_units(value, unit_from,unit_to)

    # st.write("converted value is:", result)
    # value = float(input("Enter the value you want to convert! "))
    # unit_to = input("Enter the value you want to convert from (e.g; meter, kilometer, gram, kilogram)")
    # unit_from = input("Enter the value you want to convert from (e.g; meter, kilometer, gram, kilogram)")

    # print("value>>>", value)
    # print("unit_from>>>", unit_from)
    # print("unit_to>>>", unit_to)
    # result = converte_units(value, unit_from, unit_to)
    # print("converted value is :",result)


# main()
 

import streamlit as st


# Unit convertor
def unit_convertor(value: float, unit_from: str, unit_to: str):
    print("value>>>",value)
    print("unit_from>>>",unit_from)
    print("unit_to>>>",unit_to)
    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
        return value * 0.001
    else:
        return "Conversion is not Supported!"
    
    

# result = (unit_convertor(1.5, "kilograms", "grams"))
# print("unit converted is:", result)

def main():
    st.write("Unit Convertor")
    st.text("Welcome to unit convertor!")
    print(st.write)
    print(st.text)
    value = st.number_input("Enter your value is created by a large supported(e.g; kilometers, meters, kilograms, grams, grams, kilograms)",min_value=0.0)
    unit_from = st.text_input("Enter your unit_from is created by a large supported(e.g; kilometers, meters, kilograms, grams, grams, kilograms)")
    unit_to = st.text_input("Enter your unit_to is created by a large supported(e.g; kilometers, meters, kilograms, grams, grams, kilograms)")


    if st.button("convert"):
        result = unit_convertor ("value", "unit_from", "unit_to")
        st.write("unit converted is:",result)




# result = unit_convertor ("value", "unit_from", "unit_to")
# print("unit converted is:",result)

main()











