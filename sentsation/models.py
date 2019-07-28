import numpy as np
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from .utils import bstr2array, array2bstr

class SavableSVC(SVC):
    @classmethod
    def from_super(cls, superinstance):
        if superinstance.kernel == 'linear':
            instance = cls(kernel='linear')
        else:
            instance = cls()

        instance.C = superinstance.C
        instance._dual_coef_ = superinstance._dual_coef_
        instance._gamma = superinstance._gamma
        instance._impl = superinstance._impl
        instance._intercept_ = superinstance._intercept_
        instance._sparse = superinstance._sparse
        instance.cache_size = superinstance.cache_size
        instance.class_weight = superinstance.class_weight
        instance.class_weight_ = superinstance.class_weight_
        instance.classes_ = superinstance.classes_
        instance.coef0 = superinstance.coef0
        instance.decision_function_shape = superinstance.ecision_function_shape
        instance.degree = superinstance.degree
        instance.dual_coef = superinstance.dual_coef
        instance.epsilon = superinstance.epsilon
        instance.fit_status_ = superinstance.fit_status_
        instance.gamma = superinstance.gamma
        instance.intercept_ = superinstance.intercept_
        instance.kernel = superinstance.kernel
        instance.max_iter = superinstance.max_iter
        instance.n_support_ = superinstance.n_support_
        instance.nu = superinstance.nu
        instance.probA_ = superinstance.probA_
        instance.probB_ = superinstance.probB_
        instance.probability = superinstance.probability
        instance.random_state = superinstance.random_state
        instance.shape_fit_ = superinstance.shape_fit_
        instance.shrinking = superinstance.shrinking
        instance.support_ = superinstance.support_
        instance.support_vectors_ = superinstance.support_vectors_
        instance.tol = superinstance.tol
        instance.verbose = superinstance.verbose
        return instance

    def to_super(self):
        if self.kernel == "linear":
            superinstance = SVC(kernel='linear')
        else:
            superinstance = SVC()
        
        superinstance.C = self.C
        superinstance._dual_coef_ = self._dual_coef_
        superinstance._gamma = self._gamma
        superinstance._impl = self._impl
        superinstance._intercept_ = self._intercept_
        superinstance._sparse = self._sparse
        superinstance.cache_size = self.cache_size
        superinstance.class_weight = self.class_weight
        superinstance.class_weight_ = self.class_weight_
        superinstance.classes_ = self.classes_
        superinstance.coef0 = self.coef0
        superinstance.decision_function_shape = self.decision_function_shape
        superinstance.degree = self.degree
        superinstance.dual_coef = self.dual_coef
        superinstance.epsilon = self.epsilon
        superinstance.fit_status_ = self.fit_status_
        superinstance.gamma = self.gamma
        superinstance.intercept_ = self.intercept_
        superinstance.kernel = self.kernel
        superinstance.max_iter = self.max_iter
        superinstance.n_support_ = self.n_support_
        superinstance.nu = self.nu
        superinstance.probA_ = self.probA_
        superinstance.probB_ = self.probB_
        superinstance.probability = self.probability
        superinstance.random_state = self.random_state
        superinstance.shape_fit_ = self.shape_fit_
        superinstance.shrinking = self.shrinking
        superinstance.support_ = self.support_
        superinstance.support_vectors_ = self.support_vectors_
        superinstance.tol = self.tol
        superinstance.verbose = self.verbose
        return superinstance
    
    @classmethod
    def from_dict(cls, dict_):
        kernel = dict_.get('kernel')
        instance = cls(kernel=kernel)

        instance.C = dict_.get('C')
        instance._dual_coef_ = bstr2array(dict_.get('_dual_coef_'), is_sparse=instance._sparse)
        instance.dual_coef_ = bstr2array(dict_.get('dual_coef_'), is_sparse=instance._sparse)
        #TODO: write util function to convert str to array
        instance._gamma = np.array(dict_.get('_gamma'))
        instance._impl = dict_.get('_impl')
        instance._intercept_ = dict_.get('_intercept_')
        instance._sparse = dict_.get('_sparse')
        instance.cache_size = dict_.get('cache_size')
        instance.class_weight = dict_.get('class_weight')
        instance.class_weight_ = np.array(dict_.get('class_weight_'))
        instance.classes_ = np.array(dict_.get('classes_'))
        instance.coef0 = dict_.get('coef0')
        instance.decision_function_shape = dict_.get('decision_function_shape')
        instance.degree = dict_.get('degree')
        instance.dual_coef = dict_.get('dual_coef')
        instance.epsilon = dict_.get('epsilon')
        instance.fit_status_ = dict_.get('fit_status_')
        instance.gamma = dict_.get('gamma')
        instance.intercept_ = dict_.get('intercept_')
        instance.kernel = dict_.get('kernel')
        instance.max_iter = dict_.get('max_iter')
        instance.n_support_ = np.array(dict_.get('n_support_'), dtype=np.int32)
        instance.nu = dict_.get('nu')
        instance.probA_ = dict_.get('probA_')
        instance.probB_ = dict_.get('probB_')
        instance.probability = dict_.get('probability')
        instance.random_state = dict_.get('random_state')
        instance.shape_fit_ = dict_.get('shape_fit_')
        instance.shrinking = dict_.get('shrinking')
        instance.support_ = np.array(dict_.get('support_'), dtype=np.int32)
        instance.support_vectors_ = bstr2array(dict_.get('support_vectors_'), is_sparse=instance._sparse)
        instance.tol = dict_.get('tol')
        instance.verbose = dict_.get('verbose')
        return instance

    def to_dict(self):
        dict_ = {
            'C': self.C,
            '_dual_coef_': array2bstr(self._dual_coef_, self._sparse),
            'dual_coef_': array2bstr(self.dual_coef_, self._sparse),
            #TODO write util function to convert array to str
            '_gamma': self._gamma,
            '_impl': self._impl,
            '_intercept_': self._intercept_.to_list(),
            '_sparse': array2bstr(self._sparse, self._sparse),
            'cache_size': self.cache_size,
            'class_weight': self.class_weight,
            'class_weight_': self.class_weight_.to_list(),
            'classes_': self.classes_.to_list(),
            'coef0': self.coef0,
            'decision_function_shape': self.decision_function_shape,
            'degree': self.degree,
            'dual_coef': self.dual_coef,
            'epsilon': self.epsilon,
            'fit_status_': self.fit_status_,
            'gamma': self.gamma,
            'intercept_': self.intercept_.to_list(),
            'kernel': self.kernel,
            'max_iter': self.max_iter,
            'n_support_': self.n_support_.to_list(),
            'nu': self.nu,
            'probA_': self.probA_.to_list(),
            'probB_': self.probB_.to_list(),
            'probability': self.probability,
            'random_state': self.random_state,
            'shape_fit_': self.shape_fit_,
            'shrinking': self.shrinking,
            'support_': self.support_.to_list(),
            'support_vectors_': self.support_vectors_,
            'tol': self.tol,
            'verbose': self.verbose
        }
        return dict_