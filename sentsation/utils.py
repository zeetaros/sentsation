from sklearn.model_selection import GroupShuffleSplit


def bstr2array(bstr, is_sparse):
    pass

def array2bstr(array, is_sparse):
    pass

def downsample_by_idx(df, indices, target, id_col, minority_ratio=.2):
    """
        resample the dataframe with minority_ratio, minority ratio is the number of minority/number of total
        return: array of indices that have been reduced from the input indices
    """
    df['index_col'] = df.index
    train_df = df.iloc[indices]
    to_int = lambda b: int(b)
 
    majority_ids = train_df[train_df[target].apply(to_int)==0][id_col].values
    minority_ids = train_df[train_df[target].apply(to_int)!=0][id_col].values
    
    if len(minority_ids) > len(majority_ids):
        minority_ids, majority_ids = majority_ids, minority_ids
    
    num_remain = int(((1 - minority_ratio) * len(minority_ids)) / minority_ratio)
    try:
        majority_ids_sampled = np.random.choice(majority_ids, num_remain, replace=False)
    except ValueError as e:
        print(f"Tried to sample {num_remain} out of {len(majority_ids)}")
        raise e
    train_df_sampled = train_df[train_df[id_col].isin(np.concatenate([majority_ids_sampled, minority_ids]))]
    return np.array(train_df_sampled.index_col.values)

def customised_groupshuffle(df,
                            group_by,
                            test_size=0.25,
                            n_splits=5,
                            do_downsample=False,
                            minority_ratio=None,
                            target=None,
                            random_state=None):
    """
        split data frame at a call level, to ensure no data leakage
    """
    gss = GroupShuffleSplit(train_size=1-test_size, test_size=test_size,
                            n_splits=n_splits, random_state=random_state)
    folds = gss.split(X=df, groups=df[group_by])
    for x in folds:
        train_indices, test_indices = x[0], x[1]
        if do_downsample:
            train_indices = downsample_by_idx(df=df,
                                              indices=train_indices,
                                              minority_ratio=minority_ratio,
                                              target=target,
                                              id_col=group_by)
        ids_in_train = set(df.iloc[train_indices][group_by].values)
        ids_in_test = set(df.iloc[test_indices][group_by].values)
        ids_in_both = ids_in_train.intersection(ids_in_test)
        assert not ids_in_both, f"there are some call ids in both test and train: {ids_in_both}"
        yield train_indices, test_indices
