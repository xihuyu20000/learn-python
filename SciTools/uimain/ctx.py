import typing

import pandas as pd

from core.toolkit import TableKit


class MasterMainContext:
    def __init__(self, parent):
        self.parent = parent

    def get_df(self) -> pd.DataFrame:
        return self.get_table_widget().get_dataset()

    def get_df_columns(self) -> typing.List[str]:
        return self.get_df().columns

    def get_table_widget(self) -> TableKit:
        return self.parent.clean_datatable

    def table_no_data(self) -> bool:
        return not self.get_table_widget().has_dataset()

    def master_set_clean_df(self, df, inplace_index=True, drop_index=True) -> None:
        self.parent.master_set_clean_df(df, inplace_index, drop_index)