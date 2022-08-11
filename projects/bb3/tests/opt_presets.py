#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


INIT_OPT = {
    'sdm_inference': 'greedy',
    'sdm_beam_min_length': 1,
    'sdm_beam_max_length': 10,
    'sdm_generation_take_last_newline': False,
    'sdm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'sdm_history_size': 1,
    'sdm_module': 'sdm',
    'sdm_max_prompt_len': 1912,
    'sdm_penalize_repetitions': False,
    'sdm_penalize_ctxt_repetitions': False,
    'sdm_exclude_knowledge_from_ctxt_penalty': False,
    'search_decision': 'compute',
    'search_decision_control_token': '',
    'search_decision_do_search_reply': 'search',
    'search_decision_dont_search_reply': 'do not search',
    'sdm_server': 'opt_server',
    'mdm_inference': 'greedy',
    'mdm_beam_min_length': 1,
    'mdm_beam_max_length': 10,
    'mdm_generation_take_last_newline': False,
    'mdm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'mdm_history_size': '-1',
    'mdm_module': 'mdm',
    'mdm_max_prompt_len': 1912,
    'mdm_penalize_repetitions': False,
    'mdm_penalize_ctxt_repetitions': False,
    'mdm_exclude_knowledge_from_ctxt_penalty': False,
    'memory_decision': 'compute',
    'memory_decision_control_token': '',
    'memory_decision_do_access_reply': 'access memory',
    'memory_decision_dont_access_reply': 'do not access memory',
    'memory_decision_use_memories': True,
    'mdm_server': 'opt_server',
    'search_query_control_token': '',
    'search_server': 'default',
    'sgm_generation_take_last_newline': False,
    'sgm_inference': 'greedy',
    'sgm_beam_min_length': 1,
    'sgm_beam_max_length': 32,
    'sgm_module': 'sgm',
    'sgm_max_prompt_len': 1912,
    'sgm_exclude_knowledge_from_ctxt_penalty': False,
    'sgm_penalize_repetitions': False,
    'sgm_penalize_ctxt_repetitions': False,
    'sgm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'sgm_server': 'opt_server',
    'memory_generator_control_token': '',
    'mgm_inference': 'greedy',
    'mgm_beam_min_length': 1,
    'mgm_beam_max_length': 32,
    'mgm_generation_take_last_newline': False,
    'mgm_module': 'mgm',
    'mgm_max_prompt_len': 1912,
    'mgm_exclude_knowledge_from_ctxt_penalty': False,
    'mgm_penalize_repetitions': False,
    'mgm_penalize_ctxt_repetitions': False,
    'mgm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'mgm_server': 'opt_server',
    'memory_knowledge_control_token': '',
    'mkm_inference': 'greedy',
    'mkm_beam_min_length': 1,
    'mkm_beam_max_length': 32,
    'mkm_generation_take_last_newline': False,
    'mkm_module': 'mkm',
    'mkm_max_prompt_len': 1412,
    'mkm_exclude_knowledge_from_ctxt_penalty': False,
    'mkm_penalize_ctxt_repetitions': False,
    'mkm_penalize_repetitions': True,
    'mkm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'mkm_server': 'opt_server',
    'contextual_knowledge_control_token': '',
    'contextual_knowledge_decision': 'compute',
    'ckm_inference': 'greedy',
    'ckm_beam_min_length': 1,
    'ckm_beam_max_length': 32,
    'ckm_module': 'ckm',
    'ckm_max_prompt_len': 1812,
    'ckm_generation_take_last_newline': False,
    'ckm_exclude_knowledge_from_ctxt_penalty': False,
    'ckm_penalize_ctxt_repetitions': False,
    'ckm_penalize_repetitions': True,
    'ckm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'ckm_server': 'opt_server',
    'search_knowledge_control_token': '',
    'skm_inference': 'greedy',
    'skm_beam_min_length': 1,
    'skm_beam_max_length': 64,
    'skm_module': 'skm',
    'skm_max_prompt_len': 1412,
    'skm_generation_take_last_newline': False,
    'skm_penalize_ctxt_repetitions': False,
    'skm_penalize_repetitions': True,
    'skm_exclude_knowledge_from_ctxt_penalty': False,
    'skm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'skm_server': 'opt_server',
    'srm_inference': 'factual_nucleus',
    'srm_beam_min_length': 20,
    'srm_beam_max_length': 128,
    'srm_beam_size': 1,
    'srm_generation_take_last_newline': False,
    'srm_penalize_ctxt_repetitions': True,
    'srm_penalize_repetitions': True,
    'srm_exclude_knowledge_from_ctxt_penalty': True,
    'srm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'srm_module': 'srm',
    'srm_max_prompt_len': 1784,
    'srm_server': 'opt_server',
    'crm_inference': 'factual_nucleus',
    'crm_beam_min_length': 20,
    'crm_beam_max_length': 128,
    'crm_beam_size': 1,
    'crm_generation_take_last_newline': False,
    'crm_module': 'crm',
    'crm_max_prompt_len': 1880,
    'crm_penalize_ctxt_repetitions': False,
    'crm_penalize_repetitions': True,
    'crm_exclude_knowledge_from_ctxt_penalty': True,
    'crm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'crm_server': 'opt_server',
    'mrm_inference': 'factual_nucleus',
    'mrm_beam_min_length': 20,
    'mrm_beam_max_length': 128,
    'mrm_beam_size': 1,
    'mrm_module': 'mrm',
    'mrm_max_prompt_len': 1848,
    'mrm_generation_take_last_newline': False,
    'mrm_penalize_ctxt_repetitions': False,
    'mrm_penalize_repetitions': True,
    'mrm_exclude_knowledge_from_ctxt_penalty': True,
    'mrm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'mrm_server': 'opt_server',
    'vrm_inference': 'factual_nucleus',
    'vrm_beam_min_length': 20,
    'vrm_beam_max_length': 128,
    'vrm_beam_size': 1,
    'vrm_module': 'vrm',
    'vrm_max_prompt_len': 1912,
    'vrm_generation_take_last_newline': False,
    'vrm_penalize_ctxt_repetitions': False,
    'vrm_penalize_repetitions': True,
    'vrm_exclude_knowledge_from_ctxt_penalty': False,
    'vrm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'vrm_server': 'opt_server',
    'grm_inference': 'factual_nucleus',
    'grm_beam_min_length': 20,
    'grm_beam_max_length': 128,
    'grm_beam_size': 1,
    'grm_module': 'grm',
    'grm_max_prompt_len': 1880,
    'grm_generation_take_last_newline': False,
    'grm_penalize_ctxt_repetitions': False,
    'grm_penalize_repetitions': True,
    'grm_exclude_knowledge_from_ctxt_penalty': False,
    'grm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'grm_server': 'opt_server',
    'orm_inference': 'factual_nucleus',
    'orm_beam_min_length': 1,
    'orm_beam_max_length': 128,
    'orm_beam_size': 1,
    'orm_module': 'orm',
    'orm_max_prompt_len': 1412,
    'orm_generation_take_last_newline': False,
    'orm_penalize_ctxt_repetitions': False,
    'orm_penalize_repetitions': False,
    'orm_exclude_knowledge_from_ctxt_penalty': False,
    'orm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'orm_server': 'opt_server',
    'datatype': 'valid',
    'inject_query_string': None,
    'loglevel': 'info',
    'model': 'projects.bb3.agents.opt_bb3_agent:BlenderBot3Agent',
    'beam_disregard_knowledge_for_srm_context_blocking': False,
    'exclude_context_in_skm_context_blocking': False,
    'include_knowledge_in_ckm_context_blocking': False,
    'knowledge_conditioning': 'combined',
    'num_shots': 0,
    'include_prompt': False,
    'knowledge_chunk_size': 100,
    'max_prompt_len': 1912,
    'all_vanilla_prompt': False,
}