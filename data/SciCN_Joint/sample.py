import pandas as pd 
import json 

def load_line_json(save_path):
    data = []
    with open(save_path ,'r') as f:
        for line in f.readlines():
            data.append(json.loads(line))
    f.close()
    return data

def get_bio_label(data:pd.DataFrame ,save_path= 'train.char.bio'):
    doc_count = len(data)
    entity_count = 0
    sentence_count = 0
    with open(save_path , 'w') as f:
        for row in data:
            sentence_count += len(row['sentences'])
            content = sum(row['sentences'], [])
            tags = ['O' for _ in range(len(content))]
            ner = sum(row['ner'], [])
        

            for entity in ner:
                entity_count +=1
                h, t = entity[0], entity[1]
                label = entity[2]
                span = content[h:t+1]
                tags[h] = 'B-' + label
                tags[h+1:t+1] = ['I-' + label for _ in range(t-h)]
            
            for char, tag in zip(content, tags):
                if char == '\n':
                    fmt = '{}'.format(char)
                else:
                    fmt = '{}\t{}\n'.format(char, tag)
                f.write(fmt)
                
        f.close()

        #print(span_mention , tokens_mention_span)
    print("Total Documents:" , doc_count)
    print("Total Sentences:" ,sentence_count)
    print("Total Entity :" ,entity_count)


if __name__ == '__main__':
    def sample(data, ratio=1):
        import random
        random.shuffle(data)
        return data[ :int(len(data)*ratio)]

    test_data = load_line_json('test.json')
    test_data = sample(test_data)
    get_bio_label(data=test_data, save_path='test_char.bio')


    train_data =  load_line_json('train.json')
    train_data = sample(train_data)
    get_bio_label(data=train_data, save_path='train_char.bio')


    dev_data =  load_line_json('dev.json')
    dev_data = sample(dev_data)
    get_bio_label(data=dev_data, save_path='dev_char.bio')


    

