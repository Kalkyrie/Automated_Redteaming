#####
#
# Ideas for testing: Take the 'DAN' attack. Get a LLM to think up a mild variant.
#                    For example, swapping out the DAN acromymn for another one.
#                    Then pass that attack idea to another LLM, which thinks up 10
#                    specific attack prompts.
#                    Those 10 prompts get sent to a 'target' LLM.
#                    The 10 responses are passed to a 'judge' LLM, which scores
#                    the responses.
#                    A score being 'Attack successful', 'Attack explicitly refused'
#                    or 'No useful information returned'.