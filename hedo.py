import requests
import argparse

def make_request(url, method, data=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'CACHE_INFO': '127.0.0.1',
        'CF_CONNECTING_IP': '127.0.0.1',
        'CF-Connecting-IP': '127.0.0.1',
        'CLIENT_IP': '127.0.0.1',
        'Client-IP': '127.0.0.1',
        'COMING_FROM': '127.0.0.1',
        'CONNECT_VIA_IP': '127.0.0.1',
        'FORWARD_FOR': '127.0.0.1',
        'FORWARD-FOR': '127.0.0.1',
        'FORWARDED_FOR_IP': '127.0.0.1',
        'FORWARDED_FOR': '127.0.0.1',
        'FORWARDED-FOR-IP': '127.0.0.1',
        'FORWARDED': '127.0.0.1',
        'HTTP-CLIENT-IP': '127.0.0.1',
        'HTTP-FORWARDED-FOR-IP': '127.0.0.1',
        'HTTP-PC-REMOTE-ADDR': '127.0.0.1',
        'HTTP-PROXY-CONNECTION': '127.0.0.1',
        'HTTP-VIA': '127.0.0.1',
        'HTTP-X-FORWARDED-FOR-IP': '127.0.0.1',
        'HTTP-X-IMFORWARDS': '127.0.0.1',
        'HTTP-XROXY-CONNECTION': '127.0.0.1',
        'PC_REMOTE_ADDR': '127.0.0.1',
        'PRAGMA': '127.0.0.1',
        'PROXY_AUTHORIZATION': '127.0.0.1',
        'PROXY_CONNECTION': '127.0.0.1',
        'Proxy-Client-IP': '127.0.0.1',
        'PROXY': '127.0.0.1',
        'REMOTE_ADDR': '127.0.0.1',
        'Source-IP': '127.0.0.1',
        'True-Client-IP': '127.0.0.1',
        'Via': '127.0.0.1',
        'VIA': '127.0.0.1',
        'WL-Proxy-Client-IP': '127.0.0.1',
        'X_CLUSTER_CLIENT_IP': '127.0.0.1',
        'X_COMING_FROM': '127.0.0.1',
        'X_DELEGATE_REMOTE_HOST': '127.0.0.1',
        'X_FORWARDED_FOR_IP': '127.0.0.1',
        'X_FORWARDED_FOR': '127.0.0.1',
        'X_FORWARDED': '127.0.0.1',
        'X_IMFORWARDS': '127.0.0.1',
        'X_LOCKING': '127.0.0.1',
        'X_LOOKING': '127.0.0.1',
        'X_REAL_IP': '127.0.0.1',
        'X-Backend-Host': '127.0.0.1',
        'X-BlueCoat-Via': '127.0.0.1',
        'X-Cache-Info': '127.0.0.1',
        'X-Forward-For': '127.0.0.1',
        'X-Forwarded-By': '127.0.0.1',
        'X-Forwarded-For-Original': '127.0.0.1',
        'X-Forwarded-For': '127.0.0.1, 127.0.0.1, 127.0.0.1',
        'X-Forwarded-Server': '127.0.0.1',
        'X-Forwarded-Host': '127.0.0.1',
        'X-From-IP': '127.0.0.1',
        'X-From': '127.0.0.1',
        'X-Gateway-Host': '127.0.0.1',
        'X-Host': '127.0.0.1',
        'X-Ip': '127.0.0.1',
        'X-Original-Host': '127.0.0.1',
        'X-Original-IP': '127.0.0.1',
        'X-Original-Remote-Addr': '127.0.0.1',
        'X-Original-Url': '127.0.0.1',
        'X-Originally-Forwarded-For': '127.0.0.1',
        'X-Originating-IP': '127.0.0.1',
        'X-ProxyMesh-IP': '127.0.0.1',
        'X-ProxyUser-IP': '127.0.0.1',
        'X-Real-IP': '127.0.0.1',
        'X-Remote-Addr': '127.0.0.1',
        'X-Remote-IP': '127.0.0.1',
        'X-True-Client-IP': '127.0.0.1',
        'XONNECTION': '127.0.0.1',
        'XPROXY': '127.0.0.1',
        'XROXY_CONNECTION': '127.0.0.1',
        'Z-Forwarded-For': '127.0.0.1',
        'ZCACHE_CONTROL': '127.0.0.1',
        'Base-Url': '127.0.0.1',
        'Http-Url': '127.0.0.1',
        'Proxy-Host': '127.0.0.1',
        'Proxy-Url': '127.0.0.1',
        'Real-Ip': '127.0.0.1',
        'Redirect': '127.0.0.1',
        'Referer': '127.0.0.1',
        'Referrer': '127.0.0.1',
        'Refferer': '127.0.0.1',
        'Request-Uri': '127.0.0.1',
        'Uri': '127.0.0.1',
        'Url': '127.0.0.1',
        'X-Client-IP': '127.0.0.1',
        'X-Custom-IP-Authorization': '127.0.0.1',
        'X-Forwarded-Port': '443',
        'X-Forwarded-Scheme': 'http',
        'X-Forwarded-Scheme': 'https',
        'X-Forwarder-For': '127.0.0.1',
        'X-Http-Destinationurl': '127.0.0.1',
        'X-Http-Host-Override': '127.0.0.1',
        'X-Proxy-Url': '127.0.0.1',
        'X-Rewrite-Url': '127.0.0.1',
        'X-True-IP': '127.0.0.1'
    }

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=data)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, data=data)
        elif method == 'DELETE':  # Corrected line
            response = requests.delete(url, headers=headers)
        else:
            print(f"Unsupported method: {method}")
            return
        
        print(f'Status Code: {response.status_code}')
        print('Response Headers:')
        for key, value in response.headers.items():
            print(f'{key}: {value}')
    
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

def main(url, method, exclude_methods, data):
    methods_to_try = ['GET', 'POST', 'PUT', 'DELETE']
    
    if method is None:  # If no specific method is specified
        for m in methods_to_try:
            if m not in exclude_methods:
                print(f'\n--- Trying {m} method ---')
                make_request(url, m, data)
    else:
        if method not in exclude_methods:
            make_request(url, method, data)
        else:
            print(f'Skipping excluded method: {method}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send HTTP requests with major headers.')
    parser.add_argument('-u', '--url', required=True, help='The URL to request')
    parser.add_argument('-GET', action='store_true', help='Use GET method')
    parser.add_argument('-POST', action='store_true', help='Use POST method')
    parser.add_argument('-PUT', action='store_true', help='Use PUT method')
    parser.add_argument('-DELETE', action='store_true', help='Use DELETE method')
    parser.add_argument('-e', '--exclude', nargs='*', help='Methods to exclude (e.g., -e GET POST)', default=[])
    parser.add_argument('-d', '--data', help='Data to send with POST/PUT requests')

    args = parser.parse_args()
    
    # Determine the method to use
    if args.GET:
        method = 'GET'
    elif args.POST:
        method = 'POST'
    elif args.PUT:
        method = 'PUT'
    elif args.DELETE:
        method = 'DELETE'
    else:
        method = None  # Default to trying all methods

    # Normalize excluded methods
    exclude_methods = [m.upper() for m in args.exclude]

    main(args.url, method, exclude_methods, args.data)
