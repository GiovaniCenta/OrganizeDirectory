import os
import shutil

def sortDir(dir):
    print(os.walk(dir))
    for root, dirs, files in os.walk(dir):
        for file in files:
            print(file)
            name, ext = os.path.splitext(file)
            ext = ext[1:]
            if not os.path.exists(os.path.join(dir, ext)):
                os.makedirs(os.path.join(dir, ext))
                
            
            
            if os.path.exists(os.path.join(dir, ext, file)):
                count = 1
                for newFile in os.listdir(os.path.join(dir, ext, '')):
                    if name == "_".join(newFile.split('.')[0].split('_')[:-1]):
                        count += 1
                outfile = name+'_'+str(count)+'.'+ext
            else:
                outfile = file
            print('File:', os.path.join(root, file), '->', os.path.join(dir, ext, outfile))
            try:    
                shutil.move(os.path.join(root, file), os.path.join(dir, ext, outfile))
            except FileNotFoundError:
                pass
                    
                    
                    
                    
def beginning():
    #dir = 'C://Users//Cliente//Desktop//test'
    dir = input(str("Directory to be sorted: "))
    if not os.path.isdir(dir):
        print("Directory not found")
    else:
        sortDir(dir)








if __name__ == '__main__':
    beginning()
