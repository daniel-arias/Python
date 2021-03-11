import json

def main():

    with open('C:\\Users\\DanielAR\\Desktop\\Personal\\Web Pages\\2020\\Repository\\Python\\Inputs.json') as f:
        data = json.load(f)
        # print(data)
        inputParams = {}
        # inputsType = {}
        for inputs in data['i']:

            # inputsType[inputs.split(':')[0][-1]] = inputs.split(':')[0]
            paramName = inputs.split(':')[1].split('|')[0]
            paramValue = inputs.split(':')[1].split('|')[1]
            inputParams[paramName] = paramValue
        print(len(inputParams))


if __name__ == '__main__':
    main()