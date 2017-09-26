
dmc_1997_01_248m_list_data = load_from_file(data_file_name)

dmc_pcat111_nr_3drawset_pattern = nr_3drawSet(dmc_1997_01_248m_list_data, 1,1,1)
dmc_pcat121_nr_3drawset_pattern = nr_3drawSet(dmc_1997_01_248m_list_data, 1,2,1)
dmc_pcat131_nr_3drawset_pattern = nr_3drawSet(dmc_1997_01_248m_list_data, 1,3,1)

dmc_pcat211_nr_3drawset_pattern = nr_3drawSet(dmc_1997_01_248m_list_data, 2,1,1)
dmc_pcat221_nr_3drawset_pattern = nr_3drawSet(dmc_1997_01_248m_list_data, 2,2,1)
dmc_pcat231_nr_3drawset_pattern = nr_3drawSet(dmc_1997_01_248m_list_data, 2,3,1)

dmc_pcat311_nr_3drawset_pattern = nr_3drawSet(dmc_1997_01_248m_list_data, 3,1,1)
dmc_pcat321_nr_3drawset_pattern = nr_3drawSet(dmc_1997_01_248m_list_data, 3,2,1)
dmc_pcat331_nr_3drawset_pattern = nr_3drawSet(dmc_1997_01_248m_list_data, 3,3,1)

dmc_pcat111_nr_counter_list = counter_list_3draw(dmc_pcat111_nr_3drawset_pattern)
dmc_pcat121_nr_counter_list = counter_list_3draw(dmc_pcat121_nr_3drawset_pattern)
dmc_pcat131_nr_counter_list = counter_list_3draw(dmc_pcat131_nr_3drawset_pattern)

dmc_pcat211_nr_counter_list = counter_list_3draw(dmc_pcat211_nr_3drawset_pattern)
dmc_pcat221_nr_counter_list = counter_list_3draw(dmc_pcat221_nr_3drawset_pattern)
dmc_pcat231_nr_counter_list = counter_list_3draw(dmc_pcat231_nr_3drawset_pattern)

dmc_pcat311_nr_counter_list = counter_list_3draw(dmc_pcat311_nr_3drawset_pattern)
dmc_pcat321_nr_counter_list = counter_list_3draw(dmc_pcat321_nr_3drawset_pattern)
dmc_pcat331_nr_counter_list = counter_list_3draw(dmc_pcat331_nr_3drawset_pattern)


port_counter_list_to_xls(dmc_pcat111_nr_counter_list, "111")
port_counter_list_to_xls(dmc_pcat121_nr_counter_list, "121")
port_counter_list_to_xls(dmc_pcat131_nr_counter_list, "131")

port_counter_list_to_xls(dmc_pcat211_nr_counter_list, "211")
port_counter_list_to_xls(dmc_pcat221_nr_counter_list, "221")
port_counter_list_to_xls(dmc_pcat231_nr_counter_list, "231")

port_counter_list_to_xls(dmc_pcat311_nr_counter_list, "311")
port_counter_list_to_xls(dmc_pcat321_nr_counter_list, "321")
port_counter_list_to_xls(dmc_pcat331_nr_counter_list, "331")

