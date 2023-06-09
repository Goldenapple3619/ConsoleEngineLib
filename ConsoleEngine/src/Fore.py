class Fore:
    def __init__(self, controls, iid, pos, shape, colid):
        self.Datas = {"controls":controls, "iid":iid, "pos":list(pos), "shape":shape, "collisions":colid}

    def get_iid(self) -> int:
        return self.Datas["iid"]

    def get_shape(self) -> str:
        return self.Datas["shape"]

    def get_controls(self) -> dict:
        return self.Datas["controls"]

    def get_pos(self) -> list:
        return self.Datas["pos"]


    def update_pos(self,pos) -> tuple:
        self.Datas["pos"][0] += pos[0]
        self.Datas["pos"][1] += pos[1]

        return tuple(self.Datas["pos"])

    def update_shape(self, shape) -> str:
        self.Datas["shape"] = shape

        return self.Datas["shape"]

    def set_pos(self,pos):
        self.Datas["pos"] = pos


    def check_collider(self) -> bool:
        return self.Datas["collisions"]
