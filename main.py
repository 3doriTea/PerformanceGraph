import csv
import matplotlib.pyplot as plt
import matplotlib_fontja

# plt.rcParams["font.family"] = "MS Gothic"

def plot_data(file_name : str, color : str, label : str):
    fps_data : list[int] = []
    sphere_count_data : list[int] = []

    with open(file_name, "r") as f:
        l_data = csv.reader(f, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

        for (k, v) in l_data:
            sphere_count_data.append(int(k))
            fps_data.append(int(v))
    
    plt.plot(sphere_count_data, fps_data, color=color, label=label)

plt.title('学校のゲームベース VS 自作のゲームベース')
plt.xlabel("球体の個数")
plt.ylabel("FPS")
plt.ylim(0, 60)
plt.grid()
plt.legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=0, fontsize=18)
plot_data("./SGBPerformanceOnRelease.csv", color="blue", label="自作ゲームベース")
plot_data("./GBDX11PerformanceOnRelease.csv", color="green", label="学校ゲームベース")

plt.show()
