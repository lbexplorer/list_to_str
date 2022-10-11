def list_to_str(spam=['apple', 'bananas', 'tofu', 'cate']):
    fh = ','
    for i in range(len(spam)):
        if i == 0:
            temp = str(spam[i]) + fh
            result = temp
            continue
        elif i == (len(spam) - 1):
            temp = 'and ' + str(spam[i])
            result = result + temp
            break
        temp = str(spam[i]) + fh
        result = result + temp
    return result


def main():
    list = [1, 2, 3, 4,'sada','asda']
    need_str = list_to_str(list)
    print(need_str)
    # 列表值作为参数
    pass


if __name__ == '__main__':
    main()
