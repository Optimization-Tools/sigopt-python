from .objects import ApiObject, Client, Experiment, Suggestion, Observation, Worker

class ApiResponse(ApiObject):
  pass


class ExperimentsBestObservationResponse(ApiResponse):
  @property
  def observation(self):
    _observation = self._body.get('observation')
    return Observation(_observation) if _observation else None


class ExperimentsCreateResponse(ApiResponse):
  @property
  def experiment(self):
    _experiment = self._body.get('experiment')
    return Experiment(_experiment) if _experiment is not None else None


class ExperimentResponse(ApiResponse):
  @property
  def experiment(self):
    _experiment = self._body.get('experiment')
    return Experiment(_experiment) if _experiment is not None else None


class ExperimentsSuggestResponse(ApiResponse):
  @property
  def suggestion(self):
    _suggestion = self._body.get('suggestion')
    return Suggestion(_suggestion) if _suggestion is not None else None


class ExperimentsWorkersResponse(ApiResponse):
  @property
  def workers(self):
    _workers = self._body.get('workers')
    return [Worker(w) for w in _workers]


class ClientResponse(ApiResponse):
  @property
  def client(self):
    _client = self._body.get('client')
    return Client(_client) if _client is not None else None


class ClientsExperimentsResponse(ApiResponse):
  @property
  def experiments(self):
    _experiments = self._body.get('experiments', [])
    return [Experiment(e) for e in _experiments]
