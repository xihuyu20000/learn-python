from typing import List

import pandas as pd

from core.toolkit import TableKit


class MasterMainContext:
    def __init__(self, parent):
        self.parent = parent

    def master_get_clean_df(self) -> pd.DataFrame:
        return self.parent.clean_datatable.get_dataset()

    def master_get_clean_columns(self) -> List[str]:
        return self.parent.master_get_clean_df().columns

    def master_get_clean_table(self) -> TableKit:
        return self.parent.clean_datatable

    def master_clean_no_data(self) -> bool:
        return not self.parent.clean_datatable.has_dataset()
