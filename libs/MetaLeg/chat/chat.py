import json
import time
import openai
import tiktoken
from .. import tools

globalTotalPrice = 0;

#########################################################
def basicOpenai(input):
    #-----------------------------------------------------#
    # basicOpenai faz uma requisição para a openai
    # usando o modelo gpt-3.5-turbo
    #-----------------------------------------------------#

    messages=[
        { "role": "system", "content": "Você é um robô trabalhando para a empresa Splenda IT. O trabalho principal é o tratamento e interpretação de leis brasileiras."},
        { "role": "user", "content": input},
    ]
    print("\n\n")
    print(f'{messages[0]}')
    print(messages[1]['content'])
    print("\n\n")

    input_tokens = count_tokens(messages)
    max_tokens = int(16000 - (input_tokens + (input_tokens*0.2)))
    
    if (max_tokens < 512):
        return "Seu texto excede o tamanho máximo do prompt."
    
    tentativas = 0
    resposta = ""
    
    while tentativas < 10:
        try:
            tentativas += 1
            #max_tokens=max_tokens,
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                temperature=0,
                messages=messages,
            )


            print(chat_completion)

            resposta = chat_completion.choices[0].message.content

            return(resposta)
                                    
             
        except openai.error.Timeout as e:
            print(f"OpenAI API request timed out: {e}")
            pass
        except openai.error.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
            pass
        except openai.error.APIConnectionError as e:
            print(f"OpenAI API request failed to connect: {e}")
            pass
        except openai.error.InvalidRequestError as e:
            print(f"OpenAI API request was invalid: {e}")
            pass
        except openai.error.AuthenticationError as e:
            print(f"OpenAI API request was not authorized: {e}")
            pass
        except openai.error.PermissionError as e:
            print(f"OpenAI API request was not permitted: {e}")
            pass
        except openai.error.RateLimitError as e:
            print(f"OpenAI API request exceeded rate limit: {e}")
            pass
        except openai.error.ServiceUnavailableError as e:
            print(f"OpenAI API ServiceUnavailableError: {e}")
            pass
        except Exception as e:
            print(f"Erro não previsto: {e}")
            pass
            
    
########################################################################


#########################################################
def defaultOpenai(input, title, logPath):
    #-----------------------------------------------------#
    # basicOpenai faz uma requisição para a openai
    # usando o modelo gpt-3.5-turbo
    #-----------------------------------------------------#
    start_time = time.time()


    messages=[
        { "role": "system", "content": "Você é um robô trabalhando para a empresa Splenda IT. O trabalho principal é com a ferramenta Talend Open Studio. Sua principal função como robô é criar Jobs do Talend através de arquivos JSON, XML e código JAVA."},
        { "role": "user", "content": input},
    ]

    print("\n\n")
    print(f'{messages[0]}')
    print(messages[1]['content'])
    print("\n\n")

    input_tokens = count_tokens(messages)
    max_tokens = int(16000 - (input_tokens + (input_tokens*0.2)))
    
    if (max_tokens < 512):
        return "Seu texto excede o tamanho máximo do prompt."
    
    print(title)

    tentativas = 0
    resposta = ""
    
    while tentativas < 10:
        try:
            tentativas += 1
            #max_tokens=max_tokens,
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                temperature=0,
                messages=messages,
            )

            resposta = chat_completion.choices[0].message.content
            in_tokens =  chat_completion.usage.prompt_tokens
            out_tokens =  chat_completion.usage.completion_tokens
            total_tokens  =  chat_completion.usage.total_tokens
            in_price  =  (in_tokens * 0.000003)
            out_price =  (out_tokens * 0.000004)
            total_price  =  (in_price + out_price)
            real_price  =  (total_price * 5),
            
            counter = {
                "title": title,
                "tentativas": tentativas,
                "in_tokens" : in_tokens,
                "out_tokens" : out_tokens,
                "total_tokens" : total_tokens,
                "in_price" : in_price,
                "out_price" : out_price,
                "total_price" : total_price,
                "real_price" : real_price,
            }

            print(counter)

            tools.saveProjectLog(logPath + title + '_prompt.txt', input)
            tools.saveProjectLog(logPath + title + '_response.txt', resposta)
            tools.saveProjectLog(logPath + title + '_count.txt', json.dumps(counter))

            total_time =  time.time() - start_time
            tools.saveProjectLog(logPath + title + '_time.txt', str(total_time))



            return(resposta)
             
        except openai.error.Timeout as e:
            print(f"OpenAI API request timed out: {e}")
            pass
        except openai.error.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
            pass
        except openai.error.APIConnectionError as e:
            print(f"OpenAI API request failed to connect: {e}")
            pass
        except openai.error.InvalidRequestError as e:
            print(f"OpenAI API request was invalid: {e}")
            pass
        except openai.error.AuthenticationError as e:
            print(f"OpenAI API request was not authorized: {e}")
            pass
        except openai.error.PermissionError as e:
            print(f"OpenAI API request was not permitted: {e}")
            pass
        except openai.error.RateLimitError as e:
            print(f"OpenAI API request exceeded rate limit: {e}")
            pass
        except openai.error.ServiceUnavailableError as e:
            print(f"OpenAI API ServiceUnavailableError: {e}")
            pass
        except Exception as e:
            print(f"Erro não previsto: {e}")
            pass
            
    
########################################################################


########################################################################
def count_tokens(messages, model="gpt-3.5-turbo-0301"):
    #----------------------------------------------------------#
    # num_tokens_from_messages retorna o número de tokens de um texto
    # para calcular tamanho de prompt com a API da openai.
    #----------------------------------------------------------#
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo":
        print("Warning: gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301.")
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301")
    elif model == "gpt-4":
        print("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
        return num_tokens_from_messages(messages, model="gpt-4-0314")
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif model == "gpt-4-0314":
        tokens_per_message = 3
        tokens_per_name = 1
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens
#######################################################################