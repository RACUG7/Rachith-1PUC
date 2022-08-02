from tqdm import tqdm
loop = tqdm(total=9000, position=0, leave=False)
for k in range(9000):
    loop.set_description("LOADING🔃...".format(k))
    loop.update(1)
loop.close()
print("download completed ;)")
