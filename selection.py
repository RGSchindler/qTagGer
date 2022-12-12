import re
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from target import Target
from roi import ROI



@dataclass
class Selection(ABC):
    target: Target
    regions: list[ROI] = field(init=False)

    ### Abstractmethod or Abstractclassmethod
    @abstractmethod
    def selection(self) -> list[ROI]:
        pass


class RoxP(Selection):
    target: Target
    regions: list[ROI] = field(init=False)

    def __post_init__(self) -> None:
        self.selection()

    def selection(self) -> list[ROI]:
        # roxP recognition site
        pattern = r"TAACTTTAAATAATTGGCATTATTTAAAGTTA"
        it = re.finditer(pattern, self.target.seq)
        targets = [(m.start(0), m.end(0)) for m in it]
        rois = []
        for idx, trg in enumerate(targets):
            rois.append(ROI(
                name=f"target_{idx}",
                target_start = trg[0],
                target_end = trg[1],
                genome_sequence = self.target.seq
            ))

    '''
    shutil.copyfile("settings.bak", "settings")
    with open("settings", "a") as file:
    '''