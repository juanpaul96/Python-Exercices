import time

def main():
    start_time = time.time()
    chunk_size = 400000  # lines

    def write_chunk(part, lines):
        with open('C:/Work/Python/Break Files into chunks'+ str(part) +'.csv', 'w') as f_out:
            #f_out.write(header)
            f_out.writelines(lines)
            f_out.close()

    with open('C:/Work/Catalog/BTP Migration/PyBreakFiles/data.csv', 'r') as f:
        
        parts = 1
        count = 0
        #header = f.readline()
        lines = []
        for line in f:
            count += 1
            lines.append(line)
            if count % chunk_size == 0:
                write_chunk(count // chunk_size, lines) #floor division
                lines = []
                parts += 1
        # write remainder
        if len(lines) > 0:
            write_chunk((count // chunk_size) + 1, lines)
        
        print("csv file chunked in %d parts" % parts)
        print("successfully executed in %.2f seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()