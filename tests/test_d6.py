import numpy as np
import pytest

import dice.d6 as d6


def test_encoder_expected():
    """Test encoder with all expected inputs
    """
    assert np.all(d6.nov_detect.one_hot_obs(d6.obs_cat) == np.identity(6))


def test_encoder_unexpected():
    """Test encoder with an unexpected value
    """
    with pytest.raises(ValueError):
        d6.nov_detect.one_hot_obs(np.asarray([[7]]))


def test_map_prob():
    """Test map_prob with one observation of each category
    """
    assert np.all(np.isclose(d6.model.map(d6.nov_detect.count_obs(d6.obs_cat)),
                             d6.prior_dist.mean()[np.newaxis]))
